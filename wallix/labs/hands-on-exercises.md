# Hands-On Exercises — Practice Walkthroughs

A set of **guided practice walkthroughs** mapped to the WALLIX certification curricula.
Each one gives a **Goal**, **Prerequisites**, a **conceptual outline of steps**, **what
to observe**, and an **"Explained in"** link to the relevant deep-dive.

> ⚠️ **These are practice walkthroughs, not official lab scripts.** Steps are described
> **conceptually**, based on documented WALLIX Bastion features. Exact menu paths and
> button labels are **deliberately not reproduced** (they change by version and are not
> verified here). Run these on a Bastion you have legitimate access to — the
> [WALLIX Academy lab](building-a-home-lab.md) (enrolled trainees only) or a
> partner-provided appliance. The official course labs (`Lab 2.1` … `Lab 7`) are
> referenced from the cert docs so you can line these up with them.

---

## How to use this page

- Each exercise lists the **course lab** it corresponds to (e.g. WCP-P *Lab 2.1*).
- Do them **in order** — later exercises assume the objects created earlier.
- After each, read the linked **deep-dive** to cement the *why*, then re-attempt.
- The underlying data model (users → user groups → authorization → target groups →
  targets) is the spine of everything below — keep
  [bastion-data-model](../deep-dives/bastion-data-model.md) open.

### Exercise map

| # | Exercise | Curriculum anchor | Explained in |
|---|---|---|---|
| 1 | First RDP & SSH authorization | WCA-P Lab 1 · WCP-P Lab 2.1 | [data-model](../deep-dives/bastion-data-model.md), [session-management](../deep-dives/session-management.md) |
| 2 | Password check-out / check-in | WCA-P Lab 2 · WCP-P Lab 3.1 | [secrets-and-password-management](../deep-dives/secrets-and-password-management.md) |
| 3 | Approval / four-eyes workflow | WCP-P Lab 4 | [session-management §6](../deep-dives/session-management.md#6-approval-workflows) |
| 4 | Session recording & audit | WCP-P Lab 5 | [session-management §4](../deep-dives/session-management.md#4-session-recording-and-the-audit-pipeline) |
| 5 | External authentication (LDAP/AD) | WCP-P Lab 2.4 | [authentication-and-access-manager](../deep-dives/authentication-and-access-manager.md) |
| 6 | HA database replication | WCP-P Lab 7 · WCE-P | [high-availability-and-dr](../deep-dives/high-availability-and-dr.md) |
| 7 | A REST API call | WCE-P Lab 5 | [rest-api-and-automation](../deep-dives/rest-api-and-automation.md) |

---

## Exercise 1 — First RDP & SSH authorization

**Maps to:** WCA-P *Lab 1: RDP & SSH Connections* · WCP-P *Lab 2.1*.

**Goal:** Get a user to open a proxied **RDP (Remote Desktop Protocol)** session to the
Windows Server and an **SSH (Secure Shell)** session to the Linux Server **through the
Bastion**, without the user ever knowing the target password.

**Prerequisites:**
- Bastion reachable; targets (Windows Server, Linux Server) reachable from the Bastion's
  back leg; DNS resolving (WCA-P *Lab 0: Setup DNS*).
- A Bastion user you can log in as, with a permission profile that can create objects.

**Outline of steps (conceptual):**
1. Create (or confirm) a **device** for the Windows Server and one for the Linux Server,
   each with the appropriate **service** (RDP on the Windows box, SSH on the Linux box).
2. Add a **target account** on each device (the local/AD account the Bastion will use to
   log in on the back leg) and store its secret in the **vault**.
3. Group the resources into a **target group**.
4. Put your test user into a **user group**.
5. Create the **authorization** binding that user group to that target group, granting the
   **Sessions** right and allowing the RDP / SSH protocols.
6. Log in to the **user web interface**, see the two targets, and launch each session.

**What to observe:**
- You connected **without typing the target's password** — the Bastion injected the
  vaulted credential on the back leg.
- One authorization links **exactly one** user group to **one** target group (the model's
  core rule). Remove the authorization → the target disappears from the user portal.
- The RDP session uses WALLIX's **Redemption** proxy; the SSH session is brokered text.

**Explained in:** [bastion-data-model](../deep-dives/bastion-data-model.md) (objects and
the authorization rule) and [session-management §1–3](../deep-dives/session-management.md#1-protocols-and-sub-protocols)
(protocols and the connection sequence).

---

## Exercise 2 — Password check-out / check-in

**Maps to:** WCA-P *Lab 2: Password checkout* · WCP-P *Lab 3.1*.

**Goal:** Retrieve a target credential from the vault (**check-out**), use it, then
**check it in** — observing the lock and optional forced rotation on return.

**Prerequisites:**
- Exercise 1 done (you have a vaulted target account).
- An authorization that grants the **Secrets** right (distinct from Sessions) for that
  target group.
- A **checkout policy** assigned (defines lock behaviour, duration, change-on-check-in).

**Outline of steps (conceptual):**
1. As the user, open the **password / secrets** view in the user portal and **check out**
   the target account's credential.
2. Note what the checkout returns — login + password (and SSH key / signed certificate if
   configured).
3. With **account lock** enabled in the checkout policy, try to check the same secret out
   as a second user → it is blocked while held.
4. **Check in** the secret when done.
5. If the policy has **change password at check-in**, observe that the password rotates.

**What to observe:**
- **Sessions** and **Secrets** are *separate* rights — a user can be allowed to *open a
  session* without being allowed to *see the password*, and vice-versa.
- The lock enforces **no concurrent use**; the checkout has a **duration / maximum**.
- "Change at check-in" means the next user can never reuse the password you saw.

**Explained in:** [secrets-and-password-management §1–2](../deep-dives/secrets-and-password-management.md#1-the-vault-and-what-a-checkout-returns)
(what a checkout returns; checkout policies).

---

## Exercise 3 — Approval / four-eyes workflow

**Maps to:** WCP-P *Lab 4* (Approval workflow for Session Manager and Password Manager).

**Goal:** Require a **human approval** before a privileged session (or a checkout) is
allowed — the **four-eyes** control.

**Prerequisites:**
- A working authorization from Exercise 1 or 2.
- A second user/group designated as **approver(s)**.

**Outline of steps (conceptual):**
1. On the authorization's **Approval** tab, set approval to **Approval with quorum** (N
   approvers) for connections inside the allowed time frame.
2. Optionally enable **mandatory comment**, **mandatory ticket reference**, an **approval
   timeout**, and **single (one-time) connection**.
3. As the requesting user, attempt the session/checkout → it enters a **pending** state.
4. As the approver, review and **approve** (or reject) the request.
5. Observe the requester's session/checkout proceed once approved.

**What to observe:**
- **Quorum** means *N approvers must agree*; the **self-approval** toggle decides whether
  the requester can approve their own request.
- Behaviour **inside vs. outside** the allowed time frame can differ (e.g. blocked
  outside hours).
- Every request and decision is recorded in the **Approval history** (feeds Exercise 4's
  audit).

**Explained in:** [session-management §6](../deep-dives/session-management.md#6-approval-workflows)
(approval modes, quorum, options).

---

## Exercise 4 — Session recording & audit

**Maps to:** WCP-P *Lab 5: Session Audit GUI* · WCA-P Audit module.

**Goal:** Record a privileged session and replay it; explore the audit histories and the
metadata the **Session Probe** captures.

**Prerequisites:**
- Session recording **enabled on the authorization** used in Exercise 1.
- For Windows/RDP metadata, the **Session Probe** deployed on the Windows target.

**Outline of steps (conceptual):**
1. Confirm the authorization has **session recording** toggled on.
2. Open an RDP session to the Windows Server and an SSH session to the Linux Server, do a
   few recognizable actions, then disconnect.
3. As an **auditor**, open the **session history** and **replay** the recordings in the
   embedded player.
4. Inspect the **metadata** the Session Probe collected on the RDP session (window
   titles, process start/stop, clipboard, drive file exchanges).
5. Browse the other audit views: **account history**, **approval history**, **authentication
   history**, and **connection statistics**.

**What to observe:**
- RDP/SSH is captured as **video**; textual SSH also as a searchable **transcript**.
- Recordings are **encrypted so only the originating Bastion can replay them** — this is
  why audit/recordings are **not** shared between HA nodes (see Exercise 6).
- The Session Probe **pauses keystroke capture on password fields** — passwords are not
  leaked into the recording.
- Auditors can watch a **live SSH session** even when recording is off.

**Explained in:** [session-management §4](../deep-dives/session-management.md#4-session-recording-and-the-audit-pipeline)
(recording pipeline, Session Probe, restriction rules).

---

## Exercise 5 — External authentication (LDAP / Active Directory)

**Maps to:** WCP-P *Lab 2.4: External Authentication* · WCP-P module 2.6.

**Goal:** Let users log in to the Bastion with their **directory (LDAP/AD)** credentials
instead of local Bastion accounts.

**Prerequisites:**
- A reachable **Domain Controller** (`Domain Controller` VM) with test users/groups.
- A read-capable service/bind account for the directory.

**Outline of steps (conceptual):**
1. Create an **external authentication domain** of type **LDAP / Active Directory** on the
   Bastion, pointing at the DC with the bind account and base DN (Distinguished Name).
2. Map directory groups to Bastion **user groups** so authorizations apply to AD users.
3. (Optional) Add a second factor by chaining **RADIUS** or **SAML 2.0** MFA in front.
4. Log in to the user portal as an **AD user** and confirm the mapped authorizations
   (from Exercise 1) are presented.
5. Confirm the login appears in the **authentication history**.

**What to observe:**
- The Bastion **authenticates the user against AD** but still injects **vaulted target
  credentials** on the back leg — directory login ≠ target login.
- **Account mapping** vs. **interactive login** vs. **session account** are the three ways
  the user reaches the target once authenticated (the secondary-connection modes).
- Group mapping is what scales this — you assign authorizations to *groups*, not people.

**Explained in:** [authentication-and-access-manager §1.3–1.5](../deep-dives/authentication-and-access-manager.md#13-ldap--active-directory)
(LDAP/AD, Kerberos, RADIUS) and the user-mapping modes in
[bastion-data-model §5](../deep-dives/bastion-data-model.md#5-user-mapping--secondary-connection-modes).

---

## Exercise 6 — HA (High Availability) database replication

**Maps to:** WCP-P *Lab 7: Replication* · WCE-P advanced architecture.

**Goal:** Replicate two Bastions so configuration written on one appears on the other,
using **HA Database Replication** (the v12 mechanism that replaced DRBD).

**Prerequisites:**
- **Two Bastions** of the **same version** (the WCP-P/WCE-P labs ship `Bastion #1` and
  `Bastion #2`), each reachable, **IPv4 only**.
- Root/admin CLI access on both (admin SSH on port **2242**).

**Outline of steps (conceptual):**
1. From the admin CLI, run the **`bastion-replication`** tool to create the config file,
   choosing **Master/Master** (exactly two nodes) or **Master/Slave**.
2. Provide each node's IP and the `wabadmin` / `wabsuper` credentials when prompted.
3. **Install** the replication, then run **`--monitoring`** to verify the link is healthy.
4. Create an object (e.g. a new user) on one node; confirm it appears on the other.
5. Note the **autossh SSH tunnel** carrying replication (source **3307** → destination
   **3306**).

**What to observe:**
- **Configuration data replicates**, but **audit/session tables and recordings do NOT** —
  each node keeps its own (this is by design; see Exercise 4's encryption note).
- **Master/Master is limited to exactly two nodes**; Master/Slave allows more passive
  slaves.
- All nodes must run the **same version** — a version mismatch breaks replication.

**Explained in:** [high-availability-and-dr §1–4](../deep-dives/high-availability-and-dr.md#1-why-drbd-is-gone-and-what-replaced-it)
(why DRBD is gone, topologies, the `bastion-replication` CLI, what is/ isn't replicated).

---

## Exercise 7 — A REST API call

**Maps to:** WCE-P *Lab 5: WALLIX Bastion REST API*.

**Goal:** Authenticate to the **REST (Representational State Transfer) API** and read an
object, then create one — the foundation for automation / **AAPM (Application-to-Application
Password Management)**.

**Prerequisites:**
- API access enabled on the Bastion; an **API key** (machine-to-machine) **or** a user
  account allowed to authenticate to the API.
- A client that can send HTTP requests (e.g. `curl`).

**Outline of steps (conceptual):**
1. **Authenticate.** Either send the **API key** in the request header, or open a
   user **session** (returns a cookie you reuse on later calls).
2. **Read** a resource — list users or devices — and inspect the JSON response and the
   **HTTP status code** (200 OK).
3. **Create** a resource — e.g. POST a new user — and observe **201 Created** (or **409
   Conflict** if it already exists).
4. (Stretch) **Check out** a secret via the API, use it in a script's environment without
   writing it to disk, then **check it in** (may trigger change-on-check-in).

**What to observe:**
- Your **effective rights** through the API are the **intersection** of the key's/user's
  permission profile with what the object model allows — the API does not bypass the ACL.
- Standard **REST semantics**: GET reads, POST creates, status codes signal the outcome.
- This is the real mechanism behind the "**AAPM**" marketing term — **REST API + vault
  plugins** removing hard-coded passwords from scripts (see Exercise note below).

> **Naming note:** "AAPM" and "WAAPM (WALLIX Application-to-Application Password Manager)"
> describe **using the REST API + vault** to fetch secrets at runtime. WAAPM is the
> packaged client; the underlying capability is the API you just used.

**Explained in:** [rest-api-and-automation §1–3](../deep-dives/rest-api-and-automation.md#1-authentication-to-the-api)
(API auth, resources/methods/codes, common tasks) and the AAPM/WAAPM section
[§5](../deep-dives/rest-api-and-automation.md#5-aapm--waapm--removing-hard-coded-passwords).

---

## Acronyms

| Acronym | Expansion |
|---|---|
| **PAM** | Privileged Access Management |
| **RDP** | Remote Desktop Protocol |
| **SSH** | Secure Shell |
| **ACL** | Access Control List |
| **MFA / 2FA** | Multi-Factor / Two-Factor Authentication |
| **LDAP** | Lightweight Directory Access Protocol |
| **AD** | Active Directory |
| **DN** | Distinguished Name |
| **HA** | High Availability |
| **DRBD** | Distributed Replicated Block Device (the *old* HA mechanism) |
| **REST** | Representational State Transfer |
| **API** | Application Programming Interface |
| **AAPM** | Application-to-Application Password Management |
| **WAAPM** | WALLIX Application-to-Application Password Manager |

---

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN, lab/module references): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- Repo deep-dives (feature grounding): [bastion-data-model](../deep-dives/bastion-data-model.md), [session-management](../deep-dives/session-management.md), [secrets-and-password-management](../deep-dives/secrets-and-password-management.md), [authentication-and-access-manager](../deep-dives/authentication-and-access-manager.md), [high-availability-and-dr](../deep-dives/high-availability-and-dr.md), [rest-api-and-automation](../deep-dives/rest-api-and-automation.md)
- Cert curricula: [WCA-P](../pam-bastion/wca-p-administrator.md), [WCP-P](../pam-bastion/wcp-p-professional.md), [WCE-P](../pam-bastion/wce-p-expert.md)
