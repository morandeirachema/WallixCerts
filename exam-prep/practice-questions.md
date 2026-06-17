# WALLIX PAM — Practice Questions (Unofficial Study Aid)

> **⚠️ Unofficial study questions written for practice — these are NOT actual WALLIX
> exam questions.** They were written as a pedagogical aid for self-study, grounded in
> the sourced documentation gathered in this repository (primarily the WALLIX Bastion
> **12.3.2** *Functional Administration Guide*, the Bastion **12.0.2** *Deployment
> Guide*, the WALLIX Access Manager **5.2.4.0** *Administration Guide*, the WALLIX
> Academy training catalog, and the product portfolio). They do **not** reproduce, leak,
> or simulate real WALLIX Academy exam content, and passing them guarantees nothing about
> a real exam.

This file holds **54 multiple-choice questions** organized by topic and (within each
topic) by rough difficulty. Each item gives the options, the **correct answer**, and a
short explanation pointing to where in this repo it is documented.

---

## How to use these

1. **Cover the answers.** Read the question, pick an option, then check the answer +
   explanation. The explanation links the fact back to a repo doc — follow that link to
   read the surrounding context.
2. **Learn the *why*, not the letter.** The real WALLIX final exam is a multiple-choice
   questionnaire requiring **≥ 70 %** to pass (see
   [certification-framework.md](../docs/00-overview/certification-framework.md#common-exam--assessment-model)).
   Concepts transfer; memorized answer-letters do not.
3. **Mind the version.** Several facts are version-specific (e.g. the default password
   length rose from 8 to 16 characters in **12.0.6**; DRBD was removed in **v12**). The
   questions are written against the served-document versions cited above.
4. **Topics covered:** PAM concepts · Bastion ACL data model · session management ·
   secrets/vault · authentication & Access Manager · high availability · compliance &
   standards.

Topic index:

- [A. PAM concepts & fundamentals](#a-pam-concepts--fundamentals) (Q1–Q9)
- [B. The Bastion ACL data model](#b-the-bastion-acl-data-model) (Q10–Q20)
- [C. Session management](#c-session-management) (Q21–Q31)
- [D. Secrets & the vault](#d-secrets--the-vault) (Q32–Q39)
- [E. Authentication & Access Manager](#e-authentication--access-manager) (Q40–Q48)
- [F. High availability & DR](#f-high-availability--dr) (Q49–Q52)
- [G. Compliance & standards](#g-compliance--standards) (Q53–Q54)

---

## A. PAM concepts & fundamentals

### Q1. (easy) What is the defining mechanic of a PAM gateway / bastion?

- A. The user authenticates to the gateway, which injects the target credential so the user never sees it and never has a direct path to the target
- B. It encrypts the admin's hard drive
- C. It replaces the need for Multi-Factor Authentication (MFA)
- D. It scans endpoints for malware

**Answer: A.** The user never sees the credential and never has a direct path to the
target — the credential is vaulted and injected on the brokered session. See
[what-is-pam.md](../foundations/what-is-pam.md#2-what-is-privileged-access-management-pam).

### Q2. (easy) Which of the following best describes a "privileged" account?

- A. Any account with a long password
- B. Only the Linux `root` account
- C. Any account that has logged in this week
- D. An account that can change the system, bypass controls, reach others' data, or affect many users at once

**Answer: D.** Privilege is defined by capability — administering an OS/directory,
reading anyone's data, running elevated automation, etc. See
[what-is-pam.md](../foundations/what-is-pam.md#1-first-principles-what-is-privileged-access).

### Q3. (easy) Which list correctly names the six pillars of PAM?

- A. Encrypt, compress, replicate, back up, monitor, alert
- B. Firewall, antivirus, VPN, SSO, MFA, EDR
- C. Discover & inventory; vault secrets; broker/proxy access; monitor/record sessions; audit; enforce least privilege & JIT
- D. Provision, mover, leaver, recertify, attest, report

**Answer: C.** Those are the six pillars in
[what-is-pam.md](../foundations/what-is-pam.md#4-the-pillars-of-pam). (Option D is the
IGA Joiner-Mover-Leaver / certification idea, not PAM's pillars.)

### Q4. (medium) PoLP → JIT → ZSP describes a progression. What is the end state ZSP?

- A. Zero Session Protocols — all protocols disabled
- B. Zoned Security Perimeter
- C. Zero Standing Privileges — no account holds privileged rights at rest
- D. Zero Sign-on Process

**Answer: C.** **ZSP = Zero Standing Privileges**: every privilege is acquired
Just-In-Time and disappears afterward. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md#zero-standing-privileges-zsp).

### Q5. (medium) What is the difference between Separation of Duties (SoD) and four-eyes / dual control?

- A. They are identical terms
- B. SoD applies only to cloud; four-eyes only to OT
- C. SoD splits a sensitive process across roles; four-eyes is a specific real-time form requiring two people on one action (one performs, one approves/watches)
- D. Four-eyes means using two monitors

**Answer: C.** SoD = split the process across roles; four-eyes = two people on a single
action in real time. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md#separation-of-duties-sod).

### Q6. (medium) In the identity acronym soup, which statement is correct?

- A. PAM and IAM are the same discipline
- B. IAM is the broad foundation (identity for everyone); PAM is the deep specialization for privileged access
- C. IDaaS is a governance tool that runs access-certification campaigns
- D. EPM controls remote sessions to targets

**Answer: B.** IAM is horizontal/everyday; PAM is the deep, narrow specialization. IDaaS
is a cloud *delivery model* for IAM; EPM is the *endpoint* side. See
[pam-iam-iga-idaas-epm.md](../foundations/pam-iam-iga-idaas-epm.md#1-the-one-question-test).

### Q7. (medium) "Non-repudiation" in PAM is best described as:

- A. Encrypting recordings at rest
- B. The ability to repudiate a session you did not start
- C. A type of MFA factor
- D. The property that a user cannot credibly deny what they did, because there is tamper-resistant proof — and it requires access attributed to a named individual

**Answer: D.** Non-repudiation comes from recording **plus** attribution to a named
person — which is why shared accounts are harmful. See
[core-concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md#session-recording--non-repudiation).

### Q8. (hard) Which credential-centric attack is *most directly* defeated by long, random, frequently-rotated service-account passwords stored in a vault?

- A. Phishing
- B. Kerberoasting (offline cracking of service-account tickets)
- C. A drive-by download
- D. SQL injection

**Answer: B.** Kerberoasting cracks service-ticket hashes offline; vaulting + automatic
rotation make those passwords long, random, and short-lived so they cannot be cracked in
time. See [pam-threat-landscape.md](../foundations/pam-threat-landscape.md#4-map-to-mitre-attck--how-pam-mitigates-each).

### Q9. (hard) Which statement about PAM and AD attacks (Golden Ticket / DCSync) is the most accurate, honest framing?

- A. PAM cryptographically prevents Golden Ticket forgery
- B. PAM makes the high-privilege (Domain Admin) compromise that *precedes* these attacks far harder, and makes abuse visible — but AD hardening is still required (defense-in-depth)
- C. PAM replaces the need for any AD hardening
- D. Golden Ticket is unrelated to privileged accounts

**Answer: B.** PAM is a control layer, not a magic shield; it removes the precondition
and adds visibility, but tiering / Protected Users / krbtgt rotation still matter. See
[pam-threat-landscape.md](../foundations/pam-threat-landscape.md#4-map-to-mitre-attck--how-pam-mitigates-each).

---

## B. The Bastion ACL data model

### Q10. (easy) On what data structure is the WALLIX Bastion rights engine built?

- A. Access Control Lists (ACLs)
- B. Role-Based Access Control matrices only
- C. A blockchain ledger
- D. Active Directory Group Policy Objects

**Answer: A.** The rights engine is built on **ACLs** of users, groups, devices,
services, accounts, domains, targets, target groups, and authorizations. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#key-points).

### Q11. (easy) A **target account** in WALLIX Bastion is the association of:

- A. A user + a password
- B. A user group + a target group
- C. A device, a service, and an account (or an application + account) — and the account always belongs to a domain
- D. A protocol + a port

**Answer: C.** Target account = device + service + account; **an account always belongs
to a domain**. See [bastion-data-model.md](../deep-dives/bastion-data-model.md#1-the-object-catalogue).

### Q12. (easy) A **target** (what an authorization ultimately reaches) is:

- A. Resource + target account
- B. Device + user
- C. Service + protocol
- D. Domain + policy

**Answer: A.** Target = **resource + target account**, where a resource = service +
(device or application). See [bastion-data-model.md](../deep-dives/bastion-data-model.md#1-the-object-catalogue).

### Q13. (medium) What is the cardinal rule about authorizations (an exam favourite)?

- A. One authorization can link many user groups to many target groups
- B. An authorization links a single user to a single device
- C. Authorizations are optional if profiles are set
- D. One authorization links exactly ONE user group to ONE target group; you cannot create two authorizations with the same pair

**Answer: D.** "One authorization can link only one user group to one target group … it
is not possible to create multiple authorizations with the same user group/target group
pair." See [bastion-data-model.md](../deep-dives/bastion-data-model.md#3-the-authorization-object-in-detail).

### Q14. (medium) An authorization carries two **cumulative** rights. What are they?

- A. Read and Write
- B. Admin and Auditor
- C. Sessions (open sessions) and Secrets (retrieve/view credentials)
- D. Inside and Outside

**Answer: C.** The authorization mode is *Sessions*, *Secrets*, or *Sessions and
secrets* — the two rights are cumulative. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#3-the-authorization-object-in-detail).

### Q15. (medium) Memorize the relationship chain. Which is correct?

- A. users → devices → services → ports → targets
- B. users → user groups → (authorization) → target groups → targets (resource + account)
- C. authorizations → users → domains → accounts
- D. target groups → user groups → devices → users

**Answer: B.** That is the canonical chain. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#2-entity-relationship-diagram).

### Q16. (medium) What is the difference between a **global domain** and a **local domain**?

- A. Global is cloud-hosted, local is on-prem
- B. Global domains store users; local domains store passwords
- C. There is no difference
- D. A global domain groups accounts that authenticate across multiple devices (and can use a Local or External vault); a local domain groups accounts for a single device only (Local vault)

**Answer: D.** Global = multi-device (vault Local or External); local = single device
(Local vault only). External-vault accounts are always mapped through global domains. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#4-domains--global-vs-local).

### Q17. (hard) The three secondary-connection (user-mapping) modes are:

- A. Read / Write / Execute
- B. Account mapping (user's own credential, injected); Specific/session account (vaulted, injected); Interactive login (user types it)
- C. SSH / RDP / VNC
- D. Master / Slave / Cluster

**Answer: B.** These three modes decide how the back-leg credential is obtained. Account
mapping needs `PASSWORD_MAPPING` (or a VTR); specific account needs `PASSWORD_VAULT`;
interactive needs `PASSWORD_INTERACTIVE`. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#5-user-mapping--secondary-connection-modes).

### Q18. (hard) How do **permission profiles** differ from **authorizations**?

- A. They are the same object
- B. Permission profiles decide which targets a user can reach
- C. Permission profiles govern administrative rights to GUI features (None/View/Modify), not access to targets; on conflict the highest level per feature wins
- D. Profiles can only be assigned to API keys

**Answer: C.** Profiles are a *separate axis*: they answer "can this person create users
/ edit authorizations / view audit?" — not "can they reach target X?". Highest level per
feature wins; profiles attach to users, groups, **or API keys**. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#6-permission-profiles-a-separate-axis).

### Q19. (hard) When editing an *existing* authorization, which fields are **fixed** (cannot be changed)?

- A. The protocols and sub-protocols
- B. The session-recording toggle
- C. The User group and the Target group (you must delete and recreate to re-pair)
- D. The approval quorum

**Answer: C.** The user group and target group are set at creation and cannot be changed
later. See [bastion-data-model.md](../deep-dives/bastion-data-model.md#3-the-authorization-object-in-detail).

### Q20. (hard) A **Vault Transformation Rule (VTR)** exists to:

- A. Compress recordings
- B. Rotate database root passwords
- C. Convert RDP sessions to SSH
- D. Bridge non-password primary auth (Kerberos/OIDC/SAML/X.509/SSH-key) to a vaulted secret for the back leg when account mapping is used

**Answer: D.** A VTR retrieves an existing vaulted credential for a target account
configured for account mapping, so non-password primary auth can still pull a vaulted
back-leg secret. See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#5-user-mapping--secondary-connection-modes).

---

## C. Session management

### Q21. (easy) Which protocols can the Bastion Session Manager proxy?

- A. Only SSH and RDP
- B. Only HTTPS
- C. SSH (with SFTP/sub-systems), TELNET, RLOGIN, RDP, VNC, RAW TCP/IP (Universal Tunneling), WEBAPP, and standard applications/RemoteApp via a Windows jump server
- D. FTP and SMTP only

**Answer: C.** That is the full proxy protocol set. See
[session-management.md](../deep-dives/session-management.md#1-protocols-and-sub-protocols).

### Q22. (easy) What is the RDP proxy engine in WALLIX Bastion called?

- A. xrdp
- B. FreeRDP
- C. Guacamole
- D. Redemption (WALLIX's open-source RDP proxy, the `redemption` service)

**Answer: D.** WALLIX's open-source RDP proxy is "Redemption," run by the `redemption`
service (renamed from `rdb` in 12.1.1). See
[bastion-architecture.md](../deep-dives/bastion-architecture.md#4-internal-components--services).

### Q23. (easy) Session **recordings** are encrypted such that:

- A. Anyone with the file can replay them
- B. Only the WALLIX Bastion instance that created them can replay them
- C. They are stored in plaintext
- D. Only Access Manager can decrypt them directly from the file

**Answer: B.** Recordings are Bastion-bound — only the originating Bastion can replay
them; cross-Bastion replay is brokered centrally by Access Manager (Elasticsearch search),
not by copying files. See
[session-management.md](../deep-dives/session-management.md#4-session-recording-and-the-audit-pipeline).

### Q24. (medium) What is the **Session Probe**, and on what targets does it run?

- A. A network scanner that runs on all targets
- B. An SSH key generator
- C. An RDP/Windows-only passive metadata collector that runs inside the user's session at the user's privilege; it pauses keystroke capture on password fields / UAC windows
- D. A load balancer

**Answer: C.** The Session Probe is RDP/Windows-only, passive, runs at the user's
privilege (no extra attack surface), and pauses keyboard capture on password/UAC fields.
See [session-management.md](../deep-dives/session-management.md#the-session-probe-rdp--windows-only).

### Q25. (medium) "4-eyes" vs "4-hands" in real-time monitoring means:

- A. 4-eyes = watch only (no control); 4-hands = the auditor can take control
- B. 4-eyes = two monitors; 4-hands = two keyboards
- C. They are the same
- D. 4-eyes = SSH; 4-hands = RDP

**Answer: A.** 4-eyes = monitor without control; 4-hands = gain control (RDP remote
control supported). See [session-management.md](../deep-dives/session-management.md#5-real-time-monitoring-session-sharing-and-session-invite).

### Q26. (medium) Which statement about **Session Invite** (external guest) is correct?

- A. It works for SSH, RDP, VNC, and applications on any edition
- B. It shares a live RDP or VNC session with an external guest via an expiring link, requires Access Manager 5+, and is NOT available on the WALLIX One PAM SaaS edition (and not for SSH/applications)
- C. It requires the guest to have a full Bastion account
- D. The guest gets a separate, longer timeout than the host

**Answer: B.** Session Invite is RDP/VNC only, needs Access Manager 5+, is not on SaaS,
not for SSH/applications, uses an expiring link (default 600 s), and the guest session is
bound to the host's. See [session-management.md](../deep-dives/session-management.md#session-invite-external-guest).

### Q27. (medium) Restriction rules support two actions. What are they?

- A. `allow` / `deny`
- B. `encrypt` / `decrypt`
- C. `start` / `stop`
- D. `kill` (disconnect) and `notify` (email) — matched on client-to-server data, with the most restrictive action winning across groups

**Answer: D.** Restriction rules trigger `kill` or `notify`; for RDP they can OCR window
titles via `$ocr:` / `$kbd:` prefixes. See
[session-management.md](../deep-dives/session-management.md#restriction-rules--kill--notify-and-ocr).

### Q28. (medium) Why does WALLIX recommend allowing SCP only alongside `SSH_SHELL_SESSION`, and preferring SFTP for transfer?

- A. SCP is faster
- B. SCP allows command injection (CVE-2020-15778); SFTP transfers without a shell
- C. SCP is encrypted but SFTP is not
- D. SFTP is deprecated

**Answer: B.** The guide cites CVE-2020-15778 (SCP command injection) and recommends
`SFTP_SESSION` for transfer without shell. See
[session-management.md](../deep-dives/session-management.md#1-protocols-and-sub-protocols).

### Q29. (hard) An approval workflow's Approval tab configures two independent rule sets. Inside vs. outside the time frame, the available options are:

- A. Inside: No approval / Automatic / Approval with quorum — Outside: Access blocked / Automatic / Approval with quorum
- B. Inside and outside both only offer "Approval with quorum"
- C. Inside: Access blocked only — Outside: No approval only
- D. There is only one rule set for both

**Answer: A.** Inside the frame you can require no approval, automatic, or quorum;
outside you can block, automatic, or quorum. See
[session-management.md](../deep-dives/session-management.md#6-approval-workflows).

### Q30. (hard) An approval that **starts inside** the allowed time frame but runs into blocked hours will:

- A. Be terminated the instant the time frame ends
- B. Continue — only the start time is checked against the time frame ("approval is more important than time frame"); the session ends when the approval ends
- C. Require a new approval every hour
- D. Switch automatically to interactive login

**Answer: B.** Only the **start** time is checked against the time frame; an accepted
session can continue into blocked hours. See
[session-management.md](../deep-dives/session-management.md#6-approval-workflows) and
[bastion-data-model.md](../deep-dives/bastion-data-model.md#8-runtime-evaluation-flow--how-an-authorization-is-evaluated-when-a-user-connects).

### Q31. (hard) Which type of account **cannot** be used with an authorization that includes an approval workflow?

- A. Global accounts
- B. Scenario accounts (used by an SSH startup scenario to auto-`su`/`sudo`)
- C. Device accounts
- D. Application accounts

**Answer: B.** Scenario accounts cannot be used with authorizations carrying an approval
workflow (use a separate authorization without approval). See
[bastion-data-model.md](../deep-dives/bastion-data-model.md#target-account-types) and
[session-management.md](../deep-dives/session-management.md#6-approval-workflows).

---

## D. Secrets & the vault

### Q32. (easy) What does a user **check-out** retrieve from the vault?

- A. Only a username
- B. A recording of the session
- C. Login, password, SSH private key, and (if the domain has an SSH CA) the signed SSH certificate
- D. The target's IP address only

**Answer: C.** A checkout can display login, password, SSH private key, and a signed SSH
certificate. See [secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#1-the-vault-and-what-a-checkout-returns).

### Q33. (easy) "Change password at check-in" does what?

- A. Locks the account forever
- B. Forces a password rotation when the credential is returned, so the secret the user saw is now dead (the core one-time-password pattern)
- C. Emails the password to the user
- D. Disables MFA

**Answer: B.** It rotates the secret on check-in. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#2-checkout-policies--check-out--check-in--lock--change-on-check-in).

### Q34. (medium) The **default password change policy** requires (per the 12.3.2 guide):

- A. ≥ 8 characters and RSA 2048
- B. ≥ 12 characters and ECDSA only
- C. No complexity requirements
- D. ≥ 16 characters (≥ 1 special, number, upper, lower) and RSA key size 4096 — with NO automatic scheduled rotation by default

**Answer: D.** Default = ≥ 16 chars with complexity and RSA 4096; the default minimum
rose from 8 to 16 in **12.0.6** (old policy preserved as `default (legacy)`). No automatic
scheduled rotation by default. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#3-secret-rotation-and-password-change-policies).

### Q35. (medium) What is a **reconciliation (administrator) account** used for?

- A. Approving sessions
- B. Recovering when the Bastion's stored secret has diverged from the target (so it can connect and set a new secret even when the former secret is unknown) — WALLIX recommends always providing one
- C. Storing recordings
- D. Replicating the database

**Answer: B.** The reconciliation account lets the plugin change the target secret when
the old one is unknown (drift). It is optional but recommended. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#4-password-change-plugins-and-reconciliation-accounts).

### Q36. (medium) A **password change policy** must always be coupled with what to actually rotate a secret on the target?

- A. A second user
- B. An external vault
- C. A password change **plugin** (per device type, e.g. Cisco, Windows, Unix, F5, Oracle)
- D. A SAML IdP

**Answer: C.** The policy defines the requirements/schedule; the plugin is the mechanism
that changes the secret on the target. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#3-secret-rotation-and-password-change-policies).

### Q37. (hard) Which external vault plugins does Bastion 12.3.2 support, and how are external-vault accounts mapped?

- A. Only CyberArk; mapped via local domains
- B. CyberArk Enterprise Password Vault, HashiCorp Vault (API v1), Thycotic Secret Server, and a remote Bastion Vault — mapped via global domains (Bastion retrieves only, does not rotate them)
- C. Azure Key Vault and AWS Secrets Manager; mapped via target groups
- D. None — Bastion only has its own vault

**Answer: B.** Those four external vault plugins, mapped through global domains; the
Bastion retrieves but does not rotate externally-vaulted accounts. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#5-external-vaults).

### Q38. (hard) **Break-Glass** (standard variant) delivers emergency credentials how?

- A. By printing them to a label printer
- B. By SMS
- C. By writing them to the public web GUI
- D. As a GPG-encrypted archive sent by email, automatically every night at 02:34 (Bastion's time zone), scoped to each recipient's profile; requires Credential recovery = Execute and a valid GPG key

**Answer: D.** Standard Break-Glass = nightly GPG-encrypted email at 02:34; the
*alternative* variant writes to a directory/remote storage instead. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#6-break-glass).

### Q39. (hard) "AAPM / WAAPM" (application-to-application) is technically realized by:

- A. A dedicated agent installed on every server
- B. Applications fetching the secret at runtime over the Bastion REST API (authenticating with an API key governed by a permission profile), eliminating hard-coded passwords
- C. A SAML assertion
- D. Copying secrets into environment variables at boot

**Answer: B.** AAPM is a marketing term for the REST-API + vault-plugin mechanism; the
app requests the current (rotated) secret just-in-time over the API. See
[secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md#7-aapm--waapm--application-to-application-secret-retrieval).

---

## E. Authentication & Access Manager

### Q40. (easy) In WALLIX Bastion, when is the **authorization** check performed?

- A. At the secondary (target) authentication
- B. Only when recording is enabled
- C. At the **first/primary** authentication ("the first authentication also assumes the authorization check; if there is a secondary authentication, no authorization check is performed")
- D. At session disconnect

**Answer: C.** Authorization is decided at the primary auth; a secondary factor adds
assurance but performs no authorization check. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#key-points).

### Q41. (easy) Does the Bastion itself configure full N-factor MFA?

- A. Yes, up to 10 factors natively
- B. No — it supports SFA and 2FA natively; for more than two factors WALLIX recommends delegating MFA to the IdP (SAML/OIDC) or RADIUS push
- C. Yes, but only with smart cards
- D. It does not support MFA at all

**Answer: B.** Bastion does SFA/2FA natively; true >2-factor MFA arrives via the IdP
(Entra ID, Okta, Trustelem) or RADIUS push. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#2-the-2fa--mfa-decision-model).

### Q42. (medium) Which Kerberos mode is **deprecated** in v12.X, and why?

- A. Kerberos Ticket (transparent) — too slow
- B. Both are deprecated
- C. Neither is deprecated
- D. Kerberos-Password (explicit), where the Bastion acts as a Kerberos client to fetch the ticket — deprecated due to single-point-of-failure risk; migrate to Kerberos Ticket

**Answer: D.** Kerberos-Password (explicit) is deprecated (SPOF risk); Kerberos Ticket
(transparent), where the client already holds the ticket, is recommended. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#14-kerberos--explicit-vs-transparent).

### Q43. (medium) For SAML used **with WALLIX Access Manager**, which variant is required?

- A. The Entra ID + Graph API variant
- B. Only "SAML Generic" is compatible with WAM; configuring SAML through WAM means you cannot authenticate directly to the Bastion in SAML
- C. Any SAML variant works identically
- D. SAML is not supported with WAM

**Answer: B.** "Only SAML Generic is compatible with WALLIX Access Manager." The Entra ID
+ Graph API variant is not WAM-compatible. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#18-saml-20-bastion-as-service-provider).

### Q44. (medium) Which OIDC flow does the Bastion support?

- A. Implicit Flow
- B. Authorization Code Flow only (with discovery via `.well-known/openid-configuration`; Username and Group claim mappings mandatory)
- C. Resource Owner Password Credentials
- D. Device Code Flow

**Answer: B.** Bastion supports only the OIDC Authorization Code Flow. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#19-openid-connect-oidc).

### Q45. (medium) What is WALLIX Access Manager (WAM), architecturally?

- A. A database replication tool
- B. The vault
- C. An endpoint agent
- D. An HTML5 reverse-proxy gateway in front of one or more Bastions, giving a single HTTPS entry point (no VPN, no browser plug-in); authorizations are gathered from the Bastions at each login, not stored in WAM

**Answer: D.** WAM is the HTML5 web gateway; it brokers RDP/SSH/UT over HTTPS and gathers
authorizations from registered Bastions via the REST API at login. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#3-wallix-access-manager-wam).

### Q46. (hard) In WAM's per-domain authenticator model, what do **Factor** and **Priority** mean?

- A. Factor = encryption strength; Priority = CPU scheduling
- B. Factor = the ORDER of challenge that defines the MFA chain (all must pass); Priority = HA fallback among authenticators of the SAME factor (same priority = load-balancing)
- C. They are the same field
- D. Factor = the IdP; Priority = the SP

**Answer: B.** Factor defines the MFA chain order (each must return positive); Priority
is the failover order among equivalent servers in one factor. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#34-wam-authentication-domains--factorpriority-mfa-model).

### Q47. (hard) In WAM, what is an **Organization**?

- A. A single Bastion appliance
- B. A multi-tenancy unit = a set of users and a set of Bastion instances; a user and a Bastion can belong to only one organization. The built-in `global` org's users administer but cannot connect to targets
- C. A user group
- D. A recording archive

**Answer: B.** Organizations are WAM's multi-tenancy boundary. The `global` org can
create/administer orgs but its users cannot connect to targets; `default` is the usable
one created at deploy. See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#33-multi-tenancy--organizations).

### Q48. (hard) From Bastion v12.1, WAM registers a Bastion with a scoped API-key profile. Which is the **recommended** one?

- A. `wallix_access_manager_audit` (audit only)
- B. `wallix_access_manager_session_audit` (session access + password checkout + approval management + session auditing)
- C. `wallix_access_manager_session` (no auditing)
- D. The single legacy all-in-one key

**Answer: B.** `wallix_access_manager_session_audit` is the recommended profile (covers
session, checkout, approvals, and auditing). See
[authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md#32-registering-a-bastion-in-wam).

---

## F. High availability & DR

### Q49. (easy) What replaced **DRBD** for HA in WALLIX Bastion v12?

- A. Nothing — HA was removed
- B. RAID 5
- C. Cloud snapshots
- D. HA Database Replication over an `autossh` SSH tunnel (DRBD file-system replication was removed in v12)

**Answer: D.** v12 removed DRBD; HA is now database replication over an autossh SSH
tunnel. See [high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md#1-why-drbd-is-gone-and-what-replaced-it).

### Q50. (medium) Which data is **NOT replicated** between HA nodes?

- A. Users and authorizations
- B. The audit / session tables (live data) and recordings — each node keeps its own; cross-Bastion audit comes from WAM (Elasticsearch)
- C. Devices and services
- D. Domains and target groups

**Answer: B.** Audit/session tables are live and not replicated (replicating them would
corrupt during active sessions); recordings are local to each node. See
[high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md#3-what-is-vs-is-not-replicated).

### Q51. (medium) Two HA modes exist. Which statement is correct?

- A. Master/Slave allows unlimited Slaves; Master/Master is limited to exactly two nodes
- B. Both modes are limited to two nodes
- C. Master/Master allows unlimited nodes
- D. Only Master/Slave exists

**Answer: A.** Master/Slave = one Active Master + one or more passive Slaves;
Master/Master = bidirectional but **exactly two** nodes. Managed by the
`bastion-replication` CLI. See
[high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md#2-replication-topology-diagrams).

### Q52. (hard) Which networking constraint applies to Bastion HA replication?

- A. IPv6 only
- B. IPv4 only — FQDN and IPv6 are not supported in HA configuration; the autossh tunnel rides admin SSH port 2242 and replication flows outbound 3307 → inbound 3306
- C. Any addressing, including FQDN
- D. It uses port 443 only

**Answer: B.** HA is IPv4-only (no FQDN/IPv6); the tunnel uses 2242, replication 3307→3306.
(Note: WAM itself supports IPv4 *and* IPv6 for registering Bastions — a common trap.) See
[high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md#key-points) and the
[ports cheat-sheet](../deep-dives/high-availability-and-dr.md#8-ports-cheat-sheet-ha-relevant).

---

## G. Compliance & standards

### Q53. (medium) Which sovereign security certifications does WALLIX hold on the Bastion / PAM?

- A. FIPS 140-3 and SOC 2 only
- B. Common Criteria EAL4+
- C. ANSSI CSPN (France) and BSI BSZ (Germany), with ANSSI↔BSI mutual recognition — note that no specific Common Criteria EAL level is confirmed in the sources
- D. None

**Answer: C.** ANSSI CSPN (FR) and BSI BSZ (DE) with mutual recognition; no EAL level is
confirmed. See [product-portfolio.md](../docs/00-overview/product-portfolio.md#product-certifications--standards)
and [pam-market-landscape.md](../foundations/pam-market-landscape.md#4-wallix-differentiators).

### Q54. (medium) WALLIX's placement in the major PAM analyst reports (as documented) is:

- A. Gartner Leader and KuppingerCole Niche Player
- B. Gartner Magic Quadrant **Visionary** (2023–2025, only European vendor) and KuppingerCole Leadership Compass **Overall Leader** (5th consecutive year through the 2026 edition)
- C. Not evaluated by either analyst
- D. Gartner Challenger only

**Answer: B.** Gartner = Visionary (3 consecutive years through 2025, the only European
vendor); KuppingerCole = Overall Leader (5th consecutive year, 2026 edition). See
[pam-market-landscape.md](../foundations/pam-market-landscape.md#key-points).

---

## See also

- [Cheat sheet](cheat-sheet.md) — dense quick-reference for last-minute review.
- [Certification framework](../docs/00-overview/certification-framework.md) — exam model & pass mark.
- [Bastion data model](../deep-dives/bastion-data-model.md) · [Session management](../deep-dives/session-management.md) · [Secrets & vault](../deep-dives/secrets-and-password-management.md) · [Authentication & WAM](../deep-dives/authentication-and-access-manager.md) · [HA & DR](../deep-dives/high-availability-and-dr.md)
- [Foundations](../foundations/what-is-pam.md) · [Acronyms](../reference/acronyms.md)

---

## Sources

These practice questions are grounded entirely in the repository's sourced documents:

- [docs/00-overview/product-portfolio.md](../docs/00-overview/product-portfolio.md)
- [docs/00-overview/certification-framework.md](../docs/00-overview/certification-framework.md)
- [foundations/what-is-pam.md](../foundations/what-is-pam.md), [core-concepts-least-privilege-jit-zero-trust.md](../foundations/core-concepts-least-privilege-jit-zero-trust.md), [pam-iam-iga-idaas-epm.md](../foundations/pam-iam-iga-idaas-epm.md), [privileged-accounts-and-credentials.md](../foundations/privileged-accounts-and-credentials.md), [pam-threat-landscape.md](../foundations/pam-threat-landscape.md), [pam-market-landscape.md](../foundations/pam-market-landscape.md)
- [deep-dives/bastion-data-model.md](../deep-dives/bastion-data-model.md), [bastion-architecture.md](../deep-dives/bastion-architecture.md), [session-management.md](../deep-dives/session-management.md), [secrets-and-password-management.md](../deep-dives/secrets-and-password-management.md), [authentication-and-access-manager.md](../deep-dives/authentication-and-access-manager.md), [high-availability-and-dr.md](../deep-dives/high-availability-and-dr.md)

Underlying WALLIX primary documentation those docs rely on:

- WALLIX Bastion 12.3.2 Functional Administration Guide: https://pam.wallix.one/documentation/admin-doc/bastion_en_administration_guide.pdf
- WALLIX Bastion 12.0.2 Deployment Guide: https://marketplace-wallix.s3.amazonaws.com/bastion_12.0.2_en_deployment_guide.pdf
- WALLIX Access Manager 5.2.4.0 Administration Guide: https://pam.wallix.one/documentation/admin-doc/am-admin-guide_en.pdf
- WALLIX Academy training catalog 2025–2026: https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- CVE-2020-15778 (SCP command injection): https://nvd.nist.gov/vuln/detail/CVE-2020-15778
