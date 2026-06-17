# Core Concepts: Least Privilege, JIT & Zero Trust

The vocabulary of modern access security, defined from first principles and related
to one another. These are the ideas every **Privileged Access Management (PAM)**
control implements: **Least Privilege**, **Just-In-Time access**, **Zero Standing
Privileges**, **Zero Trust / ZTNA**, **Separation of Duties**, **four-eyes / dual
control**, **session isolation**, **credential vaulting & rotation**,
**check-out/check-in**, **session recording & non-repudiation**, and **break-glass**.
Two flow diagrams show a JIT access request and a four-eyes approval.

> Builds on [what-is-pam.md](what-is-pam.md). For how attackers exploit the *absence*
> of these controls, see [pam-threat-landscape.md](pam-threat-landscape.md).

## Learning objectives

- Define each core concept in one clear sentence.
- Understand how **PoLP → JIT → ZSP** form a progression toward less standing risk.
- Place these concepts inside the **Zero Trust** model.
- Distinguish **Separation of Duties** from **four-eyes / dual control**.
- Read a **JIT request → approve → grant → auto-expire** flow and a **four-eyes
  approval** flow.

---

## 1. The concept map

These concepts are not independent — they reinforce one another. Hold this map in mind.

```
                         THE ACCESS-SECURITY CONCEPT MAP

                        ┌─────────────────────────────┐
                        │        ZERO TRUST           │  "never trust, always verify"
                        │  (the overarching mindset)  │
                        └──────────────┬──────────────┘
                                       │ realized for privileged access by ▼
        ┌──────────────────────────────────────────────────────────────────┐
        │                                                                  │
   ┌────▼─────┐   tighten   ┌────────────┐   tighten   ┌──────────────────┐│
   │  PoLP    │ ──────────► │    JIT     │ ──────────► │ ZSP              ││
   │ minimum  │   access    │ only when  │   to        │ no standing      ││
   │ rights   │   in time   │  needed    │   zero      │ privilege at all ││
   └──────────┘             └────────────┘             └──────────────────┘│
        │                                                                  │
        │   enforced & evidenced by these MECHANISMS:                      │
        │   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
        └──►│ Vaulting &   │ │ Session      │ │ Approval     │            │
            │ Rotation     │ │ Isolation +  │ │ controls:    │            │
            │ (check-out/  │ │ Recording =  │ │ SoD,         │            │
            │  check-in)   │ │ Non-repud.   │ │ four-eyes    │            │
            └──────────────┘ └──────────────┘ └──────────────┘            │
                                                  │                       │
                                       Break-glass = the audited          │
                                       emergency override of the above ───┘

   PoLP = Principle of Least Privilege   JIT = Just-In-Time   ZSP = Zero Standing Privileges
   SoD  = Separation of Duties           Non-repud. = Non-repudiation
```

---

## 2. The definitions

### Principle of Least Privilege (PoLP)

> Grant every user, process, and account the **minimum** rights needed to do its job —
> **no more**, and ideally for **no longer** than necessary.

PoLP is the foundational rule of access security (NIST SP 800-53 control **AC-6**). It
shrinks the blast radius of any compromise: an account that can do little can damage
little.

### Just-In-Time (JIT) access

> Grant privileged access **only at the moment it is needed**, for a **specific task**
> and a **limited time**, then **automatically revoke** it.

JIT is PoLP applied to *time* as well as scope. Instead of an admin holding rights 24/7
"just in case," they **request** access for a task; it is granted briefly and expires.
This shrinks the *window* of exposure to near-zero.

### Zero Standing Privileges (ZSP)

> The end-goal state where **no account holds privileged rights at rest** — every
> privilege is acquired Just-In-Time and disappears afterward.

ZSP is what you get when JIT is applied universally: there is *nothing standing* for an
attacker to steal between tasks. PoLP → JIT → ZSP is a progression from "least" to
"least *and* briefest" to "none at rest."

### Zero Trust / Zero Trust Network Access (ZTNA)

> **Zero Trust** is the security model that assumes **no implicit trust** based on
> network location — *"never trust, always verify."* Every access request is
> authenticated, authorized, and continuously evaluated, regardless of whether it comes
> from "inside" the network.

**ZTNA (Zero Trust Network Access)** is the technology pattern that applies Zero Trust
to *connectivity*: rather than dropping a user onto the network (as a VPN does), it
grants access to **specific applications/resources only**, per-session, after
verification. A PAM gateway is a natural Zero-Trust enforcement point for privileged
access: it verifies identity (often with MFA), checks authorization for *that target at
that moment*, and brokers a scoped, recorded session — no broad network access is ever
handed out. (NIST SP 800-207 defines Zero Trust Architecture.)

### Separation of Duties (SoD)

> No single person should control **all parts** of a sensitive process. Split the
> duties so that completing a high-risk action requires **more than one role**.

Classic example: the person who *requests* a privileged change should not be the same
person who *approves* it. SoD prevents both fraud and single-point error. Governance
tools (IGA/IAG) detect **SoD violations** / "toxic combinations" of rights — see the
[WALLIX IAG section](../docs/00-overview/product-portfolio.md#5-wallix-iag--identity--access-governance).

### Four-eyes / dual control

> A specific, real-time form of SoD: a sensitive action requires **two people** — one
> to perform it and one to **approve or watch** it. ("Four eyes" = two pairs.)

In PAM this appears two ways: an **approval workflow** (a second person must approve a
session before it opens) and **live session monitoring** ("4-eyes" = watch only;
"4-hands" = the supervisor can also take control). See
[Bastion real-time monitoring](../docs/00-overview/product-portfolio.md#session-management).

### Session isolation

> The user's workstation never connects **directly** to the target. The PAM gateway
> sits in the middle as a **proxy**, so the two ends are isolated.

Isolation means malware on the admin endpoint cannot ride the connection straight to
the target, and the target credential never reaches the (low-trust) workstation. This
is the **broker/proxy** pillar from [what-is-pam.md](what-is-pam.md).

### Credential vaulting & rotation

> **Vaulting** = storing secrets in an encrypted central vault instead of on endpoints,
> scripts, or sticky notes. **Rotation** = automatically changing those secrets on a
> schedule or after each use, so a leaked secret is quickly worthless.

### Check-out / check-in

> The borrow-and-return model for vaulted secrets: a user **checks out** a credential
> (optionally **locking** it so no one else can use it concurrently), uses it, then
> **checks it in** — at which point it can be **automatically rotated** ("change
> password at check-in"). This delivers per-use rotation and full attribution.

### Session recording & non-repudiation

> **Recording** captures the full privileged session (video, keystrokes, commands,
> metadata). **Non-repudiation** is the resulting property: a user **cannot credibly
> deny** what they did, because there is tamper-resistant proof.

Recording is essential for forensics, dispute resolution, and compliance — and it only
yields non-repudiation when access is **attributed to a named individual** (which is
why shared accounts are so harmful).

### Break-glass

> A pre-arranged, **highly-audited emergency override** that grants exceptional
> privileged access when normal channels fail (e.g. the approver is unreachable during
> an outage).

Break-glass is the deliberate, controlled exception to the rules above. The trade-off:
it must be **rare, alarmed, time-limited, and heavily logged**, or it becomes an
unmonitored master key (a real risk flagged for break-glass accounts in
[privileged-accounts-and-credentials.md](privileged-accounts-and-credentials.md#2-catalogue-of-privileged-account-types-with-risk)).

> **Acronyms:** **PoLP** = Principle of Least Privilege · **JIT** = Just-In-Time ·
> **ZSP** = Zero Standing Privileges · **ZTNA** = Zero Trust Network Access ·
> **SoD** = Separation of Duties · **MFA** = Multi-Factor Authentication ·
> **VPN** = Virtual Private Network. Full list:
> [reference/acronyms.md](../reference/acronyms.md).

---

## 3. FLOW — Just-In-Time access: request → approve → grant → auto-expire

A user needs privileged access to a target for a one-off task. With JIT there is **no
standing access**; they must request it, and it disappears on its own.

```
                      JIT ACCESS LIFECYCLE (one task, then gone)

   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
   │  1. REQUEST  │ ──► │  2. APPROVE  │ ──► │  3. GRANT     │ ──► │ 4. AUTO-     │
   │              │     │              │     │  (JIT)        │     │    EXPIRE     │
   └──────┬───────┘     └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
          │                    │                    │                    │
   user asks for         approver (a DIFFERENT  PAM opens a          time window ends:
   access to TARGET      person — SoD) checks   brokered, RECORDED   access REVOKED
   X for REASON Y,       the request; may       session to TARGET;   automatically;
   for DURATION Z        require a ticket /      credential INJECTED  credential ROTATED;
          │              comment / quorum       (user never sees it) session sealed in
          │                    │                    │                audit trail
          ▼                    ▼                    ▼                    │
   ┌──────────────────────────────────────────────────────────────────┐│
   │  If DENIED at step 2 → no access, request logged.                 ││
   │  If approval TIMES OUT → request expires, nothing granted.        ││
   │  Net effect: ZERO standing privilege between tasks (→ ZSP).       ││
   └──────────────────────────────────────────────────────────────────┘│
                                                                         ▼
                                                          back to NO standing access

   SoD = Separation of Duties   ZSP = Zero Standing Privileges
```

This is exactly the behaviour a PAM tool's **approval workflow + time-frame +
single-connection** options provide; in WALLIX Bastion these live on the
authorization's *Approval* tab — see
[Bastion approval / four-eyes workflows](../docs/00-overview/product-portfolio.md#session-management).

---

## 4. FLOW — four-eyes approval (dual control)

Zooming into step 2 above: a sensitive session requires a **second pair of eyes**
before it opens, and optionally a supervisor watching it live.

```
                         FOUR-EYES APPROVAL (dual control)

        REQUESTER                       APPROVER(S)                     SESSION
        ──────────                      ────────────                    ────────
            │                                │                             │
   (1) requests session ──────────────►  (2) notified of pending          │
       (target, reason,                      request                       │
        optional ticket)                     │                             │
            │                          (3) reviews; must be a              │
            │                              DIFFERENT person (SoD).          │
            │                              Options: comment required,       │
            │                              ticket required, QUORUM          │
            │                              (N approvers), timeout.          │
            │                                │                             │
            │              ┌─────────────────┴──────────────────┐          │
            │              ▼                                     ▼          │
            │        APPROVE                                  DENY          │
            │              │                                     │          │
   (4) access granted ◄────┘                                     └─► logged, no access
            │                                                                │
   (5) session opens, RECORDED ─────────────────────────────────────────────►
            │                                                                │
            │   (optional live supervision)                                  │
            │   • 4-eyes  = approver WATCHES, no control ◄────────────────── │
            │   • 4-hands = approver can TAKE CONTROL    ◄────────────────── │
            │                                                                │
   (6) on finish → session sealed in audit trail (non-repudiation)           ▼

   SoD = Separation of Duties
```

**Why two diagrams?** JIT answers *"when and for how long?"* (time-boxing access).
Four-eyes answers *"who must agree, and who is watching?"* (dual control). Real PAM
policies usually combine both: a *time-limited* session that *also* needs approval.

---

## 5. How the concepts relate (summary table)

| Concept | One-line definition | Question it answers | PAM mechanism |
|---|---|---|---|
| **PoLP** | Minimum rights only | *How much?* | Scoped authorizations |
| **JIT** | Access only when needed, then revoked | *When / how long?* | Time-frames, request workflow |
| **ZSP** | No privilege at rest | *What's left between tasks?* | JIT applied everywhere |
| **Zero Trust / ZTNA** | Never trust, always verify; per-resource access | *Should this request be trusted now?* | Gateway + MFA + per-target authZ |
| **SoD** | Split a sensitive process across roles | *Who controls the whole thing?* | Role separation, governance checks |
| **Four-eyes / dual control** | Two people for a sensitive action | *Who approves / watches?* | Approval workflow, 4-eyes/4-hands |
| **Session isolation** | Proxy between user and target | *Direct path?* | Brokered proxy |
| **Vaulting & rotation** | Encrypted store + auto-change of secrets | *Where's the secret, how fresh?* | Vault, scheduled/per-use rotation |
| **Check-out / check-in** | Borrow-and-return with optional lock + rotate | *Who has it now?* | Check-out policy |
| **Recording & non-repudiation** | Tamper-proof record of the session | *What happened, who did it?* | Session recording + named identity |
| **Break-glass** | Audited emergency override | *What if the controls block a real emergency?* | Emergency credential recovery |

---

## 6. Key takeaways

- **PoLP → JIT → ZSP** is a progression: least rights, then only when needed, then none
  at rest.
- **Zero Trust** is the umbrella mindset; a PAM gateway is a practical Zero-Trust
  enforcement point for privileged access.
- **SoD** (split duties across roles) and **four-eyes** (two people on one action) are
  related but distinct controls; PAM enforces both.
- **Vaulting + rotation + check-out/check-in** keep secrets fresh and attributable;
  **isolation + recording** give containment and **non-repudiation**.
- **Break-glass** is the deliberate, heavily-audited exception — powerful and dangerous.

---

## See also

- [What is PAM?](what-is-pam.md)
- [Privileged accounts & credentials](privileged-accounts-and-credentials.md)
- [PAM threat landscape](pam-threat-landscape.md)
- [PAM vs IAM / IGA / IDaaS / EPM / CIEM](pam-iam-iga-idaas-epm.md)
- [WALLIX product portfolio](../docs/00-overview/product-portfolio.md)
- [Acronyms](../reference/acronyms.md) · [Glossary](../reference/glossary.md)

---

## Sources

- NIST SP 800-53 Rev. 5 (AC-6 Least Privilege; AC-5 Separation of Duties): https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
- NIST — Zero Trust Architecture project / SP 1800-35: https://www.nccoe.nist.gov/projects/implementing-zero-trust-architecture
- Gartner — Just-in-Time (JIT) privileged access & glossary: https://www.gartner.com/en/information-technology/glossary/privileged-access-management-pam
- WALLIX Bastion Functional Administration Guide (served v12.3.2) — approval/four-eyes, check-out/check-in, recording: https://pam.wallix.one/documentation/admin-doc/bastion_en_administration_guide.pdf
- WALLIX Bastion product page (Zero Trust, JIT, least privilege framing): https://www.wallix.com/products/privileged-access-management/
- ISO/IEC 27001 / 27002 (access control objectives): https://www.iso.org/standard/27001
