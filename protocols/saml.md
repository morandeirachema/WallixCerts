# Security Assertion Markup Language (SAML) 2.0: how it actually works

**Security Assertion Markup Language (SAML)** is an **XML (eXtensible Markup Language)**
based open standard for exchanging **authentication** and **authorization** information
between security domains. Its dominant use is **web browser Single Sign-On (SSO)**: a user
authenticates once at a central **Identity Provider (IdP)** and then reaches many separate
**Service Providers (SPs)** — web applications — without re-entering credentials at each one.
When WALLIX **Access Manager** federates login out to a corporate IdP, or when WALLIX One
**IDaaS / Trustelem** acts *as* the IdP for a third-party SaaS app, SAML 2.0 is one of the
protocols doing that work.

This page explains the **mechanism**: who the parties are, what a SAML **assertion** is and
what it contains, how the browser carries messages between IdP and SP (**bindings**), the
full **SP-initiated SSO** message flow, and — the part you must be able to explain — *what is
signed, what is optionally encrypted, and how trust is anchored in certificates*. SAML 2.0 is
defined by the **OASIS (Organization for the Advancement of Structured Information
Standards)** SAML 2.0 specification set (Core, Bindings, Profiles, Metadata), all dated
**15 March 2005**.

> This page assumes you understand digital signatures, public/private keys, and X.509
> certificates. If not, read
> [../prerequisites/cryptography-and-pki.md](../prerequisites/cryptography-and-pki.md) first.
> SAML messages always travel inside **TLS (Transport Layer Security)** — see
> [./tls.md](tls.md).

## Learning objectives

By the end of this file you should be able to:

- Name the three **SAML roles** — IdP, SP, and the subject (the user/principal) — and the
  **assertion** that flows between them.
- Distinguish the three **statement types** an assertion can carry: **authentication**,
  **attribute**, and **authorization decision** statements.
- Explain **SP-initiated** vs **IdP-initiated** SSO and why the IdP-initiated variant is
  riskier.
- Describe the three core **bindings** — **HTTP-Redirect**, **HTTP-POST**, and **Artifact** —
  and which messages each carries.
- Walk the full **SP-initiated Web Browser SSO** flow message by message: `AuthnRequest` →
  IdP authenticates → signed `Response` POSTed to the SP **Assertion Consumer Service (ACS)**
  → application session.
- Explain how **XML Signature (XML-DSig)** gives integrity and authenticity, how optional
  **XML Encryption (XML-Enc)** gives confidentiality, and how **metadata** + certificates
  anchor trust.
- Explain **XML Signature Wrapping (XSW)**, replay, and the validation checks an SP *must*
  perform.

---

## 1. The SAML model: IdP, SP, and assertions

SAML separates the place where a user *proves who they are* from the places that *consume*
that proof.

| Role | SAML term | What it does |
|------|-----------|--------------|
| **Identity Provider (IdP)** | *Asserting party* / SAML authority | Authenticates the user (password, MFA, Kerberos, etc.) and **issues** signed assertions about them. |
| **Service Provider (SP)** | *Relying party* | The web application the user wants to reach; it **consumes** assertions and grants an application session. |
| **Subject / Principal** | *Subject* | The human user, driving a web browser, whose identity is being asserted. |

The currency exchanged between them is the **assertion**: an XML document, *issued and signed
by the IdP*, that makes claims ("statements") about a subject. The browser (or a back-channel)
carries the assertion from IdP to SP. The SP never sees the user's password — it trusts the
IdP's *signature* on the assertion instead. This indirection is the whole point of federation.

### What an assertion contains (SAML Core, §2)

A `<saml:Assertion>` element carries:

- An **`Issuer`** — the unique identifier (an **Entity ID**, usually a URI) of the IdP that
  made it.
- An optional **`<ds:Signature>`** — an **XML Signature** over the assertion (see
  [How it secures](#how-it-secures-signing-vs-encryption)).
- A **`<Subject>`** — *who* the assertion is about, including a **`<NameID>`** (the subject's
  identifier) and **`<SubjectConfirmation>`** data (e.g. method `bearer`, with a
  `Recipient`, a `NotOnOrAfter` expiry, and an `InResponseTo` linking it to the SP's request).
- **`<Conditions>`** — constraints on validity: a `NotBefore` / `NotOnOrAfter` **validity
  window**, and crucially an **`<AudienceRestriction>`** naming the SP(s) the assertion is
  intended for.
- One or more **statements** (next section).

### Three statement types

| Statement | Element | Answers | Typical content |
|-----------|---------|---------|-----------------|
| **Authentication statement** | `<AuthnStatement>` | *How and when did the IdP authenticate the user?* | Instant of authentication, session index, and an **`<AuthnContext>`** describing the method (e.g. password, MFA). |
| **Attribute statement** | `<AttributeStatement>` | *What do we know about the user?* | Name/value attributes — email, group memberships, roles, employee ID. |
| **Authorization decision statement** | `<AuthzDecisionStatement>` | *Is this subject permitted to do X on resource Y?* | A `Decision` (Permit/Deny/Indeterminate) for an action on a resource. **Note:** the OASIS spec deprecates this statement and recommends richer standards (e.g. **XACML**) for access decisions; in practice SSO uses authentication + attribute statements. |

---

## 2. SP-initiated vs IdP-initiated SSO

There are two ways an SSO flow can begin (defined in the **Web Browser SSO Profile**, SAML
Profiles §4.1):

- **SP-initiated** — the user starts at the **SP** (e.g. opens the app's URL). The SP finds
  the user is unauthenticated and **redirects the browser to the IdP** with a SAML
  `AuthnRequest` (authentication request). The IdP authenticates and sends an assertion back.
  This is the normal, recommended flow and is detailed in §4.
- **IdP-initiated** — the user starts at the **IdP** (e.g. an app launchpad/portal), picks an
  app, and the IdP sends an **unsolicited** `Response` straight to the SP's ACS. There was
  *no* `AuthnRequest`, so the assertion has **no `InResponseTo`** to bind it to a specific SP
  request.

> **Why IdP-initiated is riskier:** because there is no request to correlate against, the SP
> cannot use `InResponseTo` to detect a stolen or replayed/injected assertion. Unsolicited
> responses are a known vector for login-CSRF and assertion-injection. Prefer SP-initiated
> SSO; if IdP-initiated must be supported, the SP must enforce all other checks (signature,
> audience, conditions, one-time use) especially strictly.

---

## 3. Bindings: how messages ride the browser

A **binding** maps an abstract SAML message onto a concrete transport. The three you must
know (SAML Bindings spec):

| Binding | Channel | Carries | How |
|---------|---------|---------|-----|
| **HTTP-Redirect** | Front-channel (browser) | Small messages — typically the `AuthnRequest` | Message is **DEFLATE-compressed, Base64-encoded, URL-encoded** into a query parameter (`SAMLRequest`). Limited by URL length, so unsuitable for large signed assertions. |
| **HTTP-POST** | Front-channel (browser) | The `AuthnRequest` and especially the `Response`/assertion | Message is **Base64-encoded** into a hidden form field (`SAMLResponse`) in an auto-submitting HTML form; the browser POSTs it to the destination. Handles large, signed documents. |
| **Artifact** | Front-channel reference + back-channel resolve | A small **artifact** (a reference handle) front-channel; the real message back-channel | The IdP sends the browser a tiny `SAMLart` artifact; the SP then calls the IdP **directly** (SP↔IdP, server-to-server over TLS) via the **Artifact Resolution Protocol** to fetch the actual assertion. The sensitive assertion never traverses the browser. |

**Front-channel** = passes through the user's browser (and is therefore visible/tamperable by
anything on the client). **Back-channel** = a direct, mutually-TLS server-to-server call the
browser never sees. The Artifact binding's back-channel resolve is its security advantage; its
cost is the extra round trip and the need for direct IdP↔SP connectivity.

In a typical SSO deployment the `AuthnRequest` uses **HTTP-Redirect** and the `Response`
(carrying the assertion) uses **HTTP-POST**.

---

## 4. The full SP-initiated Web Browser SSO flow

This is the canonical flow you must be able to draw and narrate (SAML Profiles §4.1). The user
wants to reach an SP; the SP delegates authentication to the IdP and receives a **signed SAML
Response** at its **Assertion Consumer Service (ACS)** — the SP endpoint URL that "consumes"
assertions.

```mermaid
sequenceDiagram
    participant U as User / Browser
    participant SP as Service Provider (SP)
    participant IdP as Identity Provider (IdP)
    Note over U,IdP: all legs run over TLS (HTTPS)
    U->>SP: 1. GET protected resource (no session)
    SP-->>U: 2. Redirect to IdP SSO URL<br/>with SAMLRequest (AuthnRequest)<br/>+ RelayState
    Note over SP: AuthnRequest sent via<br/>HTTP-Redirect binding
    U->>IdP: 3. Follow redirect: GET SSO URL<br/>(SAMLRequest)
    Note over IdP: 4. IdP authenticates the user<br/>(password / MFA / existing session)
    IdP-->>U: 5. HTML form with SAMLResponse<br/>(signed assertion) + RelayState<br/>(HTTP-POST binding)
    U->>SP: 6. Auto-POST SAMLResponse to<br/>SP Assertion Consumer Service (ACS)
    Note over SP: 7. SP validates: XML signature,<br/>Issuer, Audience, Conditions window,<br/>InResponseTo, SubjectConfirmation,<br/>one-time use (anti-replay)
    SP-->>U: 8. Set app session cookie;<br/>redirect to original resource (RelayState)
    U->>SP: 9. GET resource (now authenticated)
```

Step by step:

1. **Access attempt.** The browser requests a protected resource at the SP; the SP has no
   local session for this user.
2. **AuthnRequest.** The SP builds a `<samlp:AuthnRequest>` (its own `Issuer`/Entity ID, the
   `AssertionConsumerServiceURL`, a unique request `ID`) and redirects the browser to the
   IdP's SSO endpoint, encoding it in the `SAMLRequest` parameter (**HTTP-Redirect**). A
   **`RelayState`** value preserves where the user was trying to go.
3. **Request arrives at IdP.** The browser follows the redirect, delivering the `AuthnRequest`
   to the IdP.
4. **IdP authenticates the user.** Using whatever method it owns — password, **Multi-Factor
   Authentication (MFA)**, Kerberos, or an *already-existing IdP session* (which is what makes
   it "single" sign-on). The user's credentials never reach the SP.
5. **Signed Response.** The IdP builds a `<samlp:Response>` containing a **signed**
   `<saml:Assertion>`. The `SubjectConfirmation` carries `InResponseTo` = the request `ID`
   from step 2, a `Recipient` = the SP's ACS URL, and a `NotOnOrAfter`. The IdP returns an
   auto-submitting HTML form (**HTTP-POST** binding) targeting the ACS.
6. **POST to the ACS.** The browser auto-submits, POSTing the `SAMLResponse` to the SP's
   **Assertion Consumer Service**.
7. **The SP validates** (the security-critical step — see §6 / Security notes).
8. **Session established.** On success the SP creates its *own* local application session
   (typically a cookie) and redirects the browser to the original resource via `RelayState`.
9. **Authenticated access** proceeds with the SP's own session; SAML's job is done.

> **`RelayState`** is opaque state the SP set in step 2 and gets back in step 6, used to
> resume the original destination. It is *not* part of the security assertion and must not be
> trusted as such; SPs should treat it as untrusted input (open-redirect risk).

---

## 5. Metadata & certificate-based trust

IdP and SP must agree, *in advance*, on each other's endpoint URLs and — critically — each
other's **signing/encryption certificates**. This configuration is exchanged as a **SAML
Metadata** document (SAML Metadata spec): an XML file describing an entity.

An `<EntityDescriptor>` contains:

- The **`entityID`** — the globally unique identifier (a URI) for the IdP or SP.
- An **`<IDPSSODescriptor>`** or **`<SPSSODescriptor>`** listing the entity's roles.
- **Endpoints** — the IdP's `SingleSignOnService` URLs (per binding); the SP's
  `AssertionConsumerService` (ACS) URLs.
- **`<KeyDescriptor>`** elements holding the entity's **X.509 certificate(s)** — tagged
  `use="signing"` and/or `use="encryption"`.

**Trust is anchored in these certificates.** When the SP receives an assertion in step 7, it
verifies the XML signature against the **public key in the IdP's metadata** that it configured
ahead of time. If that key validates the signature, the assertion genuinely came from the
trusted IdP and was not altered in transit. There is no online certificate exchange during the
flow — the certificate pinning happens at federation-setup time via metadata. (Whether the
metadata cert is a self-signed long-lived key or part of a PKI chain is deployment-specific;
many SAML deployments simply pin the exact public key from metadata rather than validating a
CA chain.)

---

## How it secures (signing vs encryption)

SAML's security rests on **three independent layers**. You must keep them distinct.

### Layer 1 — TLS for the transport

Every leg (browser↔SP, browser↔IdP, and any back-channel) runs over **TLS / HTTPS**. TLS
provides confidentiality and server authentication *on the wire* and protects the bearer
assertion while it is in transit through the browser. But TLS is hop-by-hop: it protects the
*channel*, not the *document* once it leaves the channel. That is why SAML signs the assertion
itself.

### Layer 2 — XML Signature (integrity + authenticity) — the mandatory one

The IdP signs the assertion (and/or the enclosing Response) using **XML Signature
(XML-DSig)**, a **W3C** standard that SAML profiles. Mechanically:

- The signer **canonicalizes** the signed XML (a deterministic byte form, via Exclusive
  Canonicalization) so that signature verification is not broken by insignificant XML
  formatting differences.
- It **digests** the signed element and signs that digest with the IdP's **private key**,
  embedding the result in a `<ds:Signature>` element (with `<ds:Reference>` pointing — via an
  `ID` and a digest — at exactly what is covered).
- The SP verifies the signature with the IdP's **public key from metadata** (§5).

This gives the SP two guarantees: **integrity** (the assertion's contents were not modified
after signing) and **authenticity / origin** (it really came from the IdP holding the private
key, so the SP can trust claims it never witnessed). XML Signature is what makes federation
*without* sharing the user's password possible.

> **Sign the assertion, the response, or both?** The Response and the Assertion are separately
> signable. A common hardening rule is to require the **assertion** itself to be signed (and
> ideally the response too), because signing only the outer response leaves the inner
> assertion mutable in some processing models. Misconfiguration here is the root of several
> attacks (§Security).

### Layer 3 — XML Encryption (confidentiality) — optional

XML Signature does **not** hide the assertion's contents from the browser carrying it (the
user can read their own attributes, and so can anything on the client). When attributes are
sensitive, SAML supports **XML Encryption (XML-Enc)**: the IdP encrypts the assertion (or
specific attributes) into an `<EncryptedAssertion>` using **hybrid encryption** — a fresh
symmetric content key encrypts the XML, and that symmetric key is itself encrypted to the
**SP's public key** (from the SP's `encryption` `<KeyDescriptor>` in metadata). Only the SP's
private key can unwrap it. This is *optional* and adds end-to-end confidentiality on top of
TLS.

| Mechanism | Provides | Mandatory? | Key used |
|-----------|----------|-----------|----------|
| **TLS** | Channel confidentiality + server auth (in transit) | Yes (deployment) | TLS session keys |
| **XML Signature** | **Integrity + authenticity** of the assertion | **Effectively yes for SSO** | IdP **private** key signs; SP verifies with IdP public key |
| **XML Encryption** | **Confidentiality** of assertion/attributes end-to-end | Optional | Content encrypted to SP **public** key |

**Signing ≠ encryption.** A signed-but-unencrypted assertion is *tamper-evident* but *readable*.
An encrypted-but-unsigned assertion is *secret* but *not trustworthy as to origin*. Real SSO
needs the signature; encryption is added when attribute confidentiality matters.

---

## Security notes & common attacks

- **XML Signature Wrapping (XSW).** The classic SAML attack. The attacker takes a *legitimately
  signed* assertion and restructures the XML document so that the **signature still validates
  against the original element**, while the SP's *application logic reads a different, attacker-
  injected* assertion/subject. The mismatch arises when the code that *verifies the signature*
  and the code that *extracts the subject/attributes* resolve to different elements (e.g. by
  matching on `ID` versus walking the tree). Defences: verify the signature over the **exact**
  element you then consume; reject documents with duplicate `ID`s or unexpected structure;
  use a hardened, schema-validating SAML library rather than hand-rolled XPath. XSW is the
  single most important SAML attack to be able to explain.
- **Replay.** A bearer assertion is, by definition, usable by whoever presents it. An attacker
  who captures a valid `SAMLResponse` could resubmit it. Defences the SP **must** enforce: the
  `Conditions` **`NotBefore`/`NotOnOrAfter`** window (short-lived assertions), the
  `SubjectConfirmationData` `NotOnOrAfter`, and **one-time use** — the SP records the assertion
  `ID` and rejects any `ID` seen before within the validity window.
- **The mandatory SP validation checklist.** On receiving an assertion the SP must verify, in
  effect, *all* of:
  1. **Signature** valid, against the **expected IdP key from metadata** (not a key embedded
     in the message — never trust a `KeyInfo`/certificate carried *inside* the assertion
     itself).
  2. **`Issuer`** matches the expected IdP.
  3. **`AudienceRestriction`** names *this* SP's Entity ID (an assertion minted for a different
     SP must be rejected — prevents token reuse across SPs).
  4. **`Conditions`** validity window is current; clock skew bounded.
  5. **`Recipient`** equals this SP's ACS URL, and **`InResponseTo`** matches an outstanding
     request the SP actually sent (this check is what IdP-initiated flows lose).
  6. **One-time use** (anti-replay) as above.
  Skipping any one of these is where real-world SAML breaches happen.
- **IdP-initiated risks.** Because unsolicited responses have no `InResponseTo`, they cannot be
  correlated to a request — opening the door to assertion injection and login-CSRF (logging a
  victim into an attacker-controlled identity, or vice versa). Prefer SP-initiated SSO.
- **Certificate / key hygiene.** Trust hinges on the IdP signing certificate in metadata.
  Expired, rotated-without-update, or weak (e.g. SHA-1-signed) keys break or weaken the whole
  federation. Plan metadata/cert rotation; reject weak signature algorithms.
- **`RelayState` as untrusted input.** It is attacker-influenceable and not signed; validate it
  to prevent open redirects.

For how WALLIX consumes/produces SAML in practice — Access Manager and Bastion as SAML SP, and
WALLIX One IDaaS as IdP — see
[../deep-dives/authentication-and-access-manager.md](../wallix/deep-dives/authentication-and-access-manager.md)
and [../deep-dives/idaas-trustelem.md](../wallix/deep-dives/idaas-trustelem.md). For the newer,
JSON/JWT-based federation alternative, see [./oidc-oauth2.md](oidc-oauth2.md).

---

## Sources

- **OASIS** — *Assertions and Protocols for the OASIS Security Assertion Markup Language
  (SAML) V2.0* (Core), 15 March 2005:
  <https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf>
- **OASIS** — *Bindings for the OASIS Security Assertion Markup Language (SAML) V2.0*, 15 March
  2005: <https://docs.oasis-open.org/security/saml/v2.0/saml-bindings-2.0-os.pdf>
- **OASIS** — *Profiles for the OASIS Security Assertion Markup Language (SAML) V2.0*, 15 March
  2005: <https://docs.oasis-open.org/security/saml/v2.0/saml-profiles-2.0-os.pdf>
- **OASIS** — *Metadata for the OASIS Security Assertion Markup Language (SAML) V2.0*, 15 March
  2005: <https://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf>
- **W3C** — *XML Signature Syntax and Processing*:
  <https://www.w3.org/TR/xmldsig-core/>
- **W3C** — *XML Encryption Syntax and Processing*:
  <https://www.w3.org/TR/xmlenc-core/>
- Related: [../prerequisites/cryptography-and-pki.md](../prerequisites/cryptography-and-pki.md),
  [./tls.md](tls.md), [./oidc-oauth2.md](oidc-oauth2.md),
  [../deep-dives/authentication-and-access-manager.md](../wallix/deep-dives/authentication-and-access-manager.md),
  [../deep-dives/idaas-trustelem.md](../wallix/deep-dives/idaas-trustelem.md)
