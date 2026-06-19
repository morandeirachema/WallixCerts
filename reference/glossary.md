# Glossary

> 🔁 This is the **WALLIX / PAM** glossary. For offensive / ethical-hacking terms, see the
> [CEH glossary](../ceh/reference/glossary.md) — the two are complementary, not duplicated.

An alphabetical glossary of Privileged Access Management (PAM), identity and broader
cybersecurity terms, each defined **in PAM context** for a sysadmin starting a career in
access security with WALLIX. Where a term is treated in depth elsewhere in this repo, the
entry cross-links to the relevant [foundations](../foundations/),
[deep-dives](../deep-dives/), or
[product portfolio](../docs/00-overview/product-portfolio.md) page.

For the expansions of acronyms, see [acronyms.md](acronyms.md). For how these concepts
map to regulations, see [compliance-and-standards.md](compliance-and-standards.md).

> Conventions: WALLIX-specific objects (Account, Authorization, Device, Target, etc.) are
> capitalised when referring to the Bastion data model — see
> [bastion-data-model.md](../deep-dives/bastion-data-model.md).

---

## A

**Access Control List (ACL)** — A set of rules stating which subjects may perform which
actions on which objects. WALLIX Bastion's rights engine is built on ACLs binding user
groups to target groups — see [bastion-data-model.md](../deep-dives/bastion-data-model.md).

**Access certification (recertification)** — A periodic governance review where managers
re-confirm that each person's access is still appropriate; stale rights are revoked. A
core IAG capability — see the
[IAG section](../docs/00-overview/product-portfolio.md#5-wallix-iag--identity--access-governance).

**Account (target account)** — In Bastion, the entity used to authenticate to a system
(`{device, service, account}`); it always belongs to a domain. Types include global,
local/device, application and scenario accounts.

**Agentless** — Requiring no software installed on the target. WALLIX Bastion is agentless
on targets (it proxies the protocol), which is essential in OT where PLCs/RTUs cannot host
agents. Contrast with the agent-based BestSafe endpoint model.

**Application-to-Application (A2A)** — Machine-to-machine authentication where one
application retrieves a credential to talk to another, with no human involved; the use
case behind AAPM (removing hard-coded passwords). See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md).

**Attack surface** — The total set of points an attacker could exploit. PAM shrinks it by
removing standing local-admin accounts, vaulting credentials and brokering all privileged
access. See [pam-threat-landscape.md](../foundations/pam-threat-landscape.md).

**Authentication (AuthN)** — Proving *who you are* (password, token, biometric). A PAM
gateway authenticates the human (often with MFA) before any privileged access.

**Authorization (AuthZ)** — Determining *what you may do* once authenticated. In Bastion
the **Authorization** object binds exactly one user group to one target group, carrying
**Sessions** and **Secrets** rights — see
[bastion-data-model.md](../deep-dives/bastion-data-model.md).

## B

**Bastion host / jump server** — A hardened intermediary that all privileged connections
pass through, so administrators never connect directly to targets. WALLIX Bastion *is* the
PAM bastion; see [what-is-pam.md](../foundations/what-is-pam.md) and
[bastion-architecture.md](../deep-dives/bastion-architecture.md).

**Blast radius** — How much damage a single compromise can cause. Least privilege and
session isolation keep the blast radius small.

**Break-glass** — A pre-arranged, heavily-audited emergency override that grants
exceptional privileged access when normal channels fail. Must be rare, alarmed and
time-limited. See [core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

**Broker (proxy)** — The PAM gateway sits *between* user and target, terminating the user
side and opening a separate, credential-injected connection to the target. This brokering
gives isolation, recording and credential hiding. See
[session-management.md](../deep-dives/session-management.md).

## C

**Check-out / check-in** — The borrow-and-return model for vaulted secrets: a user checks
out a credential (optionally locking it for exclusive use), uses it, then checks it in — at
which point it can be automatically rotated. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md).

**Credential** — A secret used to authenticate (password, SSH key, certificate, API key).
PAM's job is to vault, rotate and hide credentials from the human user.

**Credential injection** — The gateway supplies the target credential to the session
*directly* so the user never sees or types it; defeats credential theft from the
workstation. See [session-management.md](../deep-dives/session-management.md).

**Credential vault (secrets vault)** — An encrypted central store for passwords, SSH keys
and certificates, replacing secrets scattered on endpoints, scripts and spreadsheets. The
WALLIX Bastion Password Manager is the vault.

**Critical target** — In Bastion, a target flagged critical (on the Authorization) so it
receives extra controls such as mandatory approval. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md).

## D

**Defense in depth** — Layering multiple independent controls so no single failure is
catastrophic; PAM is one layer alongside EPM, MFA, segmentation and monitoring.

**Device** — In Bastion, physical/virtual equipment defined by name, IP/FQDN or CIDR
subnet; the basis of a Service and ultimately a Target.

**Disaster Recovery (DR)** — Restoring service after a major outage. For Bastion specifics
(replication scope, what is and isn't replicated), see
[high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md).

**Domain (global vs local)** — In Bastion, a grouping that an Account belongs to: a
**global domain** spans multiple devices (vault Local or External); a **local domain**
covers a single device. See [bastion-data-model.md](../deep-dives/bastion-data-model.md).

**Dual control (four-eyes)** — A real-time form of SoD requiring two people for a sensitive
action: one performs it, one approves/watches. In Bastion: approval workflows and
**4-eyes** (watch) / **4-hands** (take control) live monitoring. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

## E

**Elevation (privilege elevation)** — Temporarily raising a process or user to higher
rights. PEDM/EPM elevate the *specific action* rather than the whole user; see
[pam-iam-iga-idaas-epm.md](../foundations/pam-iam-iga-idaas-epm.md).

**Encryption at rest** — Protecting stored data with encryption. Bastion uses **LUKS**
(dm-crypt) for the appliance and encrypts recordings so only the originating Bastion can
replay them.

**Endpoint Privilege Management (EPM)** — Removing local-admin rights from
workstations/servers and granting per-application elevation. WALLIX delivers EPM via
**BestSafe** (privilege attached to applications, not users).

**Entitlement** — A specific right or permission granted to an identity. Governance (IGA)
maps entitlements; CIEM right-sizes them in the cloud.

## F

**Federation** — Trusting another system's authentication so a user can SSO across domains,
via SAML/OIDC. Trustelem and WAM use federation for SSO/MFA. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md).

**Four-eyes principle** — See **Dual control**.

## G

**Gateway** — See **Broker (proxy)** and **Bastion host**. WALLIX Access Manager is also a
web gateway/reverse proxy in front of one or more Bastions.

**Governance** — The discipline of deciding and proving *who should have access*; delivered
by IGA/IAG (access reviews, SoD, compliance reporting), distinct from the IAM plumbing that
*operates* access.

## H

**Hardening** — Reducing a system's attack surface by removing unneeded services,
tightening configuration and applying secure defaults; expected of a bastion appliance.

**High Availability (HA)** — Configuration that avoids single points of failure. In Bastion
v12, HA is database replication (Master/Slave or Master/Master) over an SSH tunnel; audit
and session tables are *not* replicated. See
[high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md).

## I

**Identity** — The digital representation of a person, service or machine. IAM manages
identities; PAM controls the *privileged* subset of what they can do.

**Identity & Access Governance (IAG/IGA)** — The governance overlay (access reviews, SoD,
remediation, compliance). WALLIX IAG is the acquired Kleverware product; see
[pam-iam-iga-idaas-epm.md](../foundations/pam-iam-iga-idaas-epm.md).

**Identity-as-a-Service (IDaaS)** — Cloud-delivered IAM (SSO/MFA/federation). WALLIX
delivers it via Trustelem / WALLIX One IDaaS.

**Just-in-Time, see JIT (filed under J).**

## J

**Joiner-Mover-Leaver (JML)** — The identity lifecycle: onboarding, role change,
offboarding. Governance recertifies access at each transition (especially "mover") to
prevent privilege accumulation.

**Jump server (jump host)** — See **Bastion host**.

**Just-In-Time (JIT) access** — Granting privileged access only at the moment it is needed,
for a specific task and limited time, then auto-revoking it. PoLP applied to *time*. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

## L

**Lateral movement** — An attacker's technique of hopping from one compromised host to
others, typically by reusing harvested credentials. Session isolation, credential hiding
and least privilege break the chain. See
[pam-threat-landscape.md](../foundations/pam-threat-landscape.md).

**Least privilege (PoLP)** — Granting the minimum rights needed, for no longer than
necessary (NIST SP 800-53 AC-6); the foundational rule of access security. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

## M

**Multi-Factor Authentication (MFA)** — Requiring two or more independent factors (know /
have / are). A PAM gateway typically requires MFA before privileged access; WALLIX provides
MFA via Trustelem / WALLIX Authenticator. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md).

## N

**Non-human identity (machine identity)** — A service account, application or bot that
authenticates without a person. These vastly outnumber humans and are managed via vaulting,
rotation and AAPM. See
[privileged-accounts-and-credentials.md](../foundations/privileged-accounts-and-credentials.md).

**Non-repudiation** — The property that a user cannot credibly deny what they did, because
tamper-resistant, individually-attributed evidence (session recording) exists. Requires
named accounts, not shared ones.

## O

**Orphan account** — An account whose owner has left or is unknown, left active by mistake;
a prime attacker foothold. Governance (IAG) discovers and remediates orphan/over-entitled
accounts.

**Over-privileged (over-entitled)** — Holding more rights than the role needs; the gap
least privilege and access reviews aim to close.

## P

**Pass-the-Hash (PtH)** — An attack that authenticates using a stolen password *hash*
without cracking it, enabling lateral movement on Windows. PAM mitigates it by hiding
credentials, rotating secrets and not exposing hashes to the workstation. See
[pam-threat-landscape.md](../foundations/pam-threat-landscape.md).

**Pass-the-Ticket (PtT)** — Similar to Pass-the-Hash but reusing a stolen Kerberos ticket.

**Permission profile** — In Bastion, the object governing *administrative* rights
(None/View/Modify per feature), assignable to users, groups or API keys — distinct from
target authorizations.

**Privilege Elevation & Delegation Management (PEDM)** — Elevating a specific
command/application rather than the whole user; least privilege at the action level.

**Privileged access** — Access that can change, control or destroy systems and data
(admin/root, network gear, databases, hypervisors). The "dangerous" subset PAM exists to
control. See [what-is-pam.md](../foundations/what-is-pam.md).

**Privileged Access Management (PAM)** — The discipline of controlling, vaulting,
brokering, recording and auditing privileged access. WALLIX delivers it via Bastion. See
[what-is-pam.md](../foundations/what-is-pam.md).

**Privileged account** — An account with elevated rights (e.g. `root`, `Administrator`,
`sa`, network-device enable, service accounts). Catalogued by risk in
[privileged-accounts-and-credentials.md](../foundations/privileged-accounts-and-credentials.md).

**Privileged Access Governance (PAG)** — IGA governance applied specifically to privileged
accounts (pairing WALLIX IAG with Bastion).

**Proxy** — See **Broker**.

**Purdue Model** — A reference model layering industrial networks (Levels 0–5). A PAM
jump/bastion host typically sits in the **Industrial DMZ (Level 3.5)** between OT and IT.
See [acronyms.md](acronyms.md) and the
[PAM4OT section](../docs/00-overview/product-portfolio.md#6-wallix-pam4ot--operational-technology-ot-security).

## R

**Reconciliation account** — A privileged "administrator" account the PAM tool uses to
reset/fix a target credential when its vaulted value has drifted out of sync with the
target. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md).

**Resource** — In Bastion, a Service combined with a Device or Application; combined with a
target Account it forms a **Target**. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md).

**Reverse proxy** — A server that fronts internal services and forwards requests to them;
WALLIX Access Manager is an HTML5 reverse proxy in front of Bastion(s).

**Role-Based Access Control (RBAC)** — Granting access by assigning users to roles that
bundle permissions, simplifying administration and reviews.

**Rotation (credential rotation)** — Automatically changing secrets on a schedule or after
each use, so a leaked secret quickly becomes worthless. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md).

## S

**Scenario account** — In Bastion, an account that automates a privilege step (e.g.
`su`/`sudo`) at the start of an SSH session.

**Secret** — Any sensitive authentication material: password, SSH key, certificate, API
token. Stored in the vault, never on endpoints. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md).

**Segregation/Separation of Duties (SoD)** — Splitting a sensitive process so no single
person controls all of it (e.g. requester ≠ approver). Governance detects "toxic
combinations". See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

**Session isolation** — The user's workstation never connects directly to the target; the
PAM gateway proxies in between, isolating the two ends so malware can't ride the connection
and the credential never reaches the workstation.

**Session recording** — Capturing a privileged session (video, keystrokes, commands,
metadata) for forensics, dispute resolution and compliance; the basis of non-repudiation.
Bastion encrypts recordings to the originating Bastion. See
[session-management.md](../deep-dives/session-management.md).

**Service** — In Bastion, a protocol + port + connection policy on a Device.

**Service account** — A non-human account used by an application/service to run or
authenticate; often over-privileged and rarely rotated, hence a prime PAM target.

**Single Sign-On (SSO)** — Authenticate once and reach many trusting apps via federation
(SAML/OIDC). A usability *and* security win (fewer passwords to phish).

**Standing privilege** — Privileged rights held continuously "at rest", available to be
stolen between tasks. JIT/ZSP aim to eliminate standing privilege.

**Sub-protocol** — In Bastion, a granular, authorization-gated capability within a protocol
(e.g. SSH: shell, SCP, SFTP, X11; RDP: clipboard, drive, printer). See
[session-management.md](../deep-dives/session-management.md).

## T

**Target** — In Bastion, a **Resource + a target Account** — i.e. *what* a user is
authorized to reach. The unit authorizations are granted against. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md).

**Target group** — A collection of similar Targets that share authorizations.

**Toxic combination** — A pairing of entitlements that together enable fraud or abuse,
violating SoD (e.g. create a vendor *and* approve its payment); flagged by governance.

## U

**User mapping (account mapping)** — A Bastion secondary-connection mode where the user
reaches the target with *their own* directory credentials, injected automatically. Contrast
with a vault-stored "specific account" or manual "interactive login". See
[bastion-data-model.md](../deep-dives/bastion-data-model.md).

## V

**Vaulting** — Storing secrets in an encrypted central vault rather than on endpoints,
scripts or notes. See **Credential vault** and
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md).

## Z

**Zero Standing Privileges (ZSP)** — The end-state where no account holds privileged rights
at rest; every privilege is acquired Just-In-Time and disappears afterward. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

**Zero Trust** — The security model that assumes no implicit trust based on network
location: *"never trust, always verify."* Every access request is authenticated,
authorized and continuously evaluated. A PAM gateway is a practical Zero-Trust enforcement
point for privileged access. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md).

**Zero Trust Network Access (ZTNA)** — Applying Zero Trust to connectivity: granting
per-session access to *specific* resources after verification, rather than dropping a user
onto the network as a VPN does.

---

## See also

- [Acronyms](acronyms.md) — expansions of every abbreviation used above.
- [Compliance & standards](compliance-and-standards.md) — how PAM maps to regulations.
- [What is PAM?](../foundations/what-is-pam.md)
- [Core concepts: least privilege, JIT, Zero Trust](../foundations/core-concepts-least-privilege-jit-zero-trust.md)
- [Privileged accounts & credentials](../foundations/privileged-accounts-and-credentials.md)
- [PAM threat landscape](../foundations/pam-threat-landscape.md)
- [Bastion data model](../deep-dives/bastion-data-model.md)
- [WALLIX product portfolio](../docs/00-overview/product-portfolio.md)

---

## Sources

- WALLIX product portfolio (this repo, with primary WALLIX sources): [../docs/00-overview/product-portfolio.md](../docs/00-overview/product-portfolio.md)
- WALLIX Bastion Administration Guide (served v12.3.2) — data-model objects, sessions, recording, check-out/check-in, reconciliation: https://pam.wallix.one/documentation/admin-doc/bastion_en_administration_guide.pdf
- WALLIX Access Manager Administration Guide (served v5.2.4.0): https://pam.wallix.one/documentation/admin-doc/am-admin-guide_en.pdf
- WALLIX Bastion product page (broker/vault/record/JIT framing): https://www.wallix.com/products/privileged-access-management/
- NIST SP 800-53 Rev. 5 (AC-6 least privilege; AC-5 separation of duties): https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
- Gartner — PAM glossary (privileged access, JIT): https://www.gartner.com/en/information-technology/glossary/privileged-access-management-pam
- MITRE ATT&CK — Pass-the-Hash (T1550.002) / Pass-the-Ticket (T1550.003): https://attack.mitre.org/techniques/T1550/
