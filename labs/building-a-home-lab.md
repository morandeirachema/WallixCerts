# Building a Home Lab for WALLIX PAM Practice

How a learner can get hands-on with **PAM (Privileged Access Management)** and
**WALLIX Bastion** while studying for the certifications. This page separates what is
**officially provided by WALLIX Academy** (gated to enrolled trainees) from what you can
**build yourself** to practise the surrounding skills.

> ⚠️ **No fabrication policy.** This is a study compilation, not a WALLIX publication.
> Where the WALLIX Bastion software itself is needed, you must obtain it through WALLIX
> or a partner — there is **no verified public free download** of the appliance. Lab
> access on the WALLIX Academy platform is **provided only to enrolled trainees**.
> Where something needs WALLIX/partner access, this page says so plainly.

---

## Key points

- The **official labs come with the training** — Azure-hosted **VMs (Virtual Machines)**
  for instructor-led courses, and a downloadable **OVA (Open Virtualization Appliance /
  Open Virtual Appliance)** image for e-learning. **Both are restricted to enrolled
  trainees.**
- The documented lab topology is a small Windows/Linux estate fronted by WALLIX:
  **Domain Controller + Windows Server + Linux Server + 2× Bastion + 1× Access Manager**.
- Minimum hardware for the OVA lab (per the cert datasheets): **i5-class 4-CPU machine,
  32 GB RAM, ~40 GB free disk** — see [WCP-P](../docs/pam-bastion/wcp-p-professional.md#lab-environment).
- You **cannot legally spin up your own Bastion appliance without it** — the OVA, cloud
  Marketplace image, or ISO all come through WALLIX/partner channels. **Confirm
  availability with WALLIX or your reseller.**
- You **can** build the *substrate* (AD + Windows + Linux) yourself for free, so that the
  day a Bastion is dropped in front of it, you already understand both legs of the proxy.

---

## 1. The official WALLIX Academy lab environments

WALLIX Academy provides **preconfigured lab platforms** as part of the course; you do not
assemble the Bastion yourself. There are two delivery shapes, matching the two course
formats described in the [certification framework](../docs/00-overview/certification-framework.md#labs):

| Course format | Lab delivery | Where it runs | Access |
|---|---|---|---|
| **Instructor-led** (`WCA-P`, `WCP-P`, `WCE-P`) | Preconfigured VMs hosted on **Microsoft Azure** | WALLIX cloud (you connect remotely) | Enrolled trainees only |
| **E-learning** (`eWCA-P`, `eWCP-P`, `eWCE-P`, `eWCP-I`, `eWCP-G`) | Downloadable **OVA** image(s) run on **your own laptop** | Your local hypervisor | Enrolled trainees only |

Notes that matter for planning:

- The **e-learning** format requires **administrator rights on your own laptop** to
  install the hypervisor and import the OVA (per the cert prerequisites).
- The **OT** course (`eWCP-P-OT`) uses **demos rather than a full VM lab** — no separate
  lab hardware list is specified (see [eWCP-P-OT](../docs/ot-pam4ot/ewcp-p-ot-professional.md#prerequisites)).
- These environments are **not a public download**. If you are not enrolled, you do not
  get the OVA. Do not look for a "free trial appliance" link — none is verified here.

---

## 2. The documented lab topology

The PAM courses share one core topology, sized up or down per level. Boxes below are
the VMs WALLIX provides preconfigured. Counts are taken directly from the cert docs:

- **WCA-P** — 4 VMs (DC + Windows Server + Linux + **1 Bastion**); Azure for
  instructor-led, OVA for e-learning. See [WCA-P lab environment](../docs/pam-bastion/wca-p-administrator.md#lab-environment).
- **WCP-P** — **6 VMs** (DC + Windows Server + Linux + **2 Bastion** + **1 Access
  Manager**). See [WCP-P lab environment](../docs/pam-bastion/wcp-p-professional.md#lab-environment).
- **WCE-P** — **5 VMs** (DC + Windows Server + Linux + **2 Bastion**; no separate Access
  Manager VM). See [WCE-P lab environment](../docs/pam-bastion/wce-p-expert.md#lab-environment).

### FLOW — WCP-P lab topology (the fullest PAM lab)

```
                        ADMIN WORKSTATION (your laptop / RDP-SSH client)
                                          |
                                          | HTTPS 443 (user web portal)
                                          | SSH 22 / RDP 3389 (proxied sessions)
                                          v
   +--------------------------------------------------------------------------+
   |                          WALLIX FRONT-END (entry point)                  |
   |                                                                          |
   |   +-------------------------+        +-------------------------------+   |
   |   |   Access Manager (WAM)  |        |        Bastion #1             |   |
   |   |   HTML5 reverse proxy   |------->|   (PAM proxy / vault / GUI)   |   |
   |   |   single HTTPS gateway  |        |   Session + Password Mgr      |   |
   |   +-------------------------+        +-------------------------------+   |
   |                                              |                          |
   |                                              | HA Database Replication  |
   |                                              v                          |
   |                                      +-------------------------------+  |
   |                                      |        Bastion #2             |  |
   |                                      |   (HA peer / replica)         |  |
   |                                      +-------------------------------+  |
   +--------------------------------------------------------------------------+
                          |  BACK LEG (Bastion -> target)
                          |  SSH 22 / RDP 3389, credentials injected
        +-----------------+-----------------+----------------------------+
        |                 |                                              |
        v                 v                                              v
 +--------------+  +------------------+                        +------------------+
 | Domain       |  | Windows Server   |                        | Linux Server     |
 | Controller   |  | 2016             |                        | (SSH target)     |
 | (AD/DNS/     |  | (RDP target /    |                        |                  |
 |  Kerberos)   |  |  jump server)    |                        |                  |
 | Win 2016     |  |                  |                        |                  |
 +--------------+  +------------------+                        +------------------+
        ^                 ^                                              ^
        |                 |                                              |
        +-----------------+----------------------------------------------+
                  AD domain: users, DNS, Kerberos KDC for all hosts
```

**How to read it:** users never touch the targets directly. They authenticate to the
**front leg** (WAM or Bastion), and the Bastion opens the **back leg** to the target,
injecting the vaulted credential. The two-legged model is explained in
[bastion-architecture](../deep-dives/bastion-architecture.md#2-front-leg-vs-back-leg--the-two-legged-connection-model);
the AD/Kerberos roles in [windows-and-active-directory](../prerequisites/windows-and-active-directory.md).

### Hardware (cite the cert docs)

| Cert | Minimum (from datasheet) |
|---|---|
| **WCA-P** (instructor-led) | **i5, 8 GB RAM** (you only run a remote client) |
| **WCA-P / WCP-P / WCE-P** (OVA e-learning) | **4 CPU / i5, 32 GB RAM, 40 GB free** |
| **eWCP-I** (IDaaS OVA) | **4 CPU / i5, 32 GB RAM, 40 GB free** (2 VMs + a tenant) |
| **eWCP-G** (IAG OVA) | **i5, 16 GB RAM, 50 GB free**; reserve ≥2 cores / 4 GB in VirtualBox |

The 32 GB RAM figure is the binding constraint for the PAM OVA labs — running 5–6 VMs
on one laptop is memory-hungry. (Sources: the cert datasheets linked above.)

---

## 3. Obtaining WALLIX Bastion software (outside the gated lab)

If you want to practise on a Bastion **beyond the course window**, the appliance must
come from WALLIX or a partner. The deployment guide documents these **virtual-appliance
delivery channels** (see [bastion-architecture §5](../deep-dives/bastion-architecture.md#5-appliance-types-and-deployment-options)):

| Channel | What it is | Caveat |
|---|---|---|
| **AWS Marketplace** (AMI, BYOL) | Bastion virtual appliance listing on AWS | Listing exists; **licence/BYOL applies** — pricing **not specified here**. Confirm current terms on AWS Marketplace. |
| **Azure Marketplace** | Bastion virtual appliance image | Listed in the deployment guide as a cloud image. Confirm availability/terms with WALLIX. |
| **GCP / Alibaba / Outscale** | Cloud Marketplace images | Listed in the deployment guide. |
| **On-prem hypervisor images** | KVM, Hyper-V, Nutanix AHV, OpenStack, VMware vSphere | A platform-specific image, or a **generic GPG-signed ISO**. Obtained via WALLIX/partner. |
| **WALLIX One PAM (SaaS)** | Bastion + Access Manager managed by WALLIX | Subscription; not a download. |

> **Be explicit:** "the listing exists" is **not** the same as "free." Every channel
> above is **BYOL (Bring Your Own Licence)** or subscription. There is **no verified free
> personal/learning licence** for Bastion in the sources used here. To get a usable
> licence key, **check with WALLIX or your reseller/partner** (`academy@wallix.com` for
> training-related access). Do not assume cloud-Marketplace deployment is free of charge.

---

## 4. Hypervisor options for running OVA / your own VMs

Any of these can host the OVA (when you have it) or your self-built substrate VMs:

| Hypervisor | Notes for a home lab |
|---|---|
| **Oracle VirtualBox** | Free, cross-platform; the IAG datasheet explicitly references VirtualBox core/RAM reservations, so it is a known-good OVA host. |
| **Microsoft Hyper-V** | Built into Windows Pro/Enterprise; good if your laptop already runs Windows. Also a Bastion deployment target. |
| **VMware Workstation / Player / ESXi / vSphere** | Strong OVA support; vSphere (≥ ESXi 5.5) is a documented Bastion deployment platform. |
| **KVM/QEMU** | Free on Linux; a documented Bastion deployment platform. |
| **Cloud (AWS / Azure / GCP)** | Pay-as-you-go; lets you avoid the 32 GB-RAM laptop requirement. Mind running costs. |

For importing an OVA, "Import Appliance" (VirtualBox/VMware) or the hypervisor's import
flow is the generic path — exact menu wording varies by tool and is **not reproduced
here** to avoid fabrication.

---

## 5. What you can practise WITHOUT WALLIX (build the substrate)

Even with no Bastion, you can build the **environment a Bastion protects**, which is
where most exam-relevant prerequisite skills live. This costs nothing but evaluation
licences/time and prepares both legs of the proxy.

### FLOW — self-built substrate (no WALLIX software required)

```
   +---------------------------------------------------------------+
   |                 YOUR FREE HOME LAB (no Bastion yet)           |
   |                                                               |
   |   +------------------+   AD domain    +-------------------+   |
   |   | Domain Controller|<-------------->| Windows Server    |   |
   |   | Win Server eval  |  DNS/Kerberos  | (member server,   |   |
   |   | (AD DS + DNS)    |                |  RDP target)      |   |
   |   +------------------+                +-------------------+   |
   |            ^                                   ^              |
   |            | LDAP / Kerberos                   | RDP 3389     |
   |            v                                   |              |
   |   +------------------+                         |              |
   |   | Linux Server     |<------------------------+              |
   |   | (Debian/Ubuntu)  |   SSH 22                                |
   |   | sshd + sudo +    |                                         |
   |   | optional SSSD    |   <-- where Bastion's "back leg" would  |
   |   |  joined to AD    |       land once installed               |
   |   +------------------+                                         |
   +---------------------------------------------------------------+
              (drop a Bastion + Access Manager in front later)
```

What to practise on this substrate, mapped to the deep-dives:

- **Active Directory** — stand up **AD DS (Active Directory Domain Services)** + **DNS
  (Domain Name System)**, create users/groups, understand **Kerberos** and
  service accounts. → [windows-and-active-directory](../prerequisites/windows-and-active-directory.md).
- **Linux targets** — `sshd`, key vs. password auth, `sudo`, `su`, and joining Linux to
  AD (SSSD) — exactly what a Bastion **scenario account** automates at session start.
  → [linux-essentials-for-pam](../prerequisites/linux-essentials-for-pam.md).
- **Networking & protocols** — SSH/RDP/TLS, ports, proxy/gateway placement in a DMZ
  (Demilitarized Zone). → [networking-and-protocols](../prerequisites/networking-and-protocols.md).
- **Crypto & PKI** — TLS certificates, SSH keys, RSA key sizes — the same primitives
  Bastion uses for the front/back legs. → [cryptography-and-pki](../prerequisites/cryptography-and-pki.md).
- **PAM concepts** — least privilege, JIT (Just-in-Time), Zero Trust applied to the
  accounts you just created. → [foundations](../foundations/what-is-pam.md).

When you later add a Bastion (via a course OVA or a partner-provided image), this
substrate becomes its **target estate**, and the [hands-on exercises](hands-on-exercises.md)
become directly runnable.

---

## Acronyms

| Acronym | Expansion |
|---|---|
| **PAM** | Privileged Access Management |
| **VM** | Virtual Machine |
| **OVA** | Open Virtualization Appliance / Open Virtual Appliance |
| **WAM** | WALLIX Access Manager |
| **HA** | High Availability |
| **DC** | Domain Controller |
| **AD (DS)** | Active Directory (Domain Services) |
| **DNS** | Domain Name System |
| **DMZ** | Demilitarized Zone |
| **AMI** | Amazon Machine Image |
| **BYOL** | Bring Your Own Licence |
| **JIT** | Just-in-Time (access) |
| **SSSD** | System Security Services Daemon (Linux↔AD) |

---

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- Bastion Deployment Guide (v12.0.2, appliance/deployment channels): https://marketplace-wallix.s3.amazonaws.com/bastion_12.0.2_en_deployment_guide.pdf
- WALLIX Bastion on AWS Marketplace: https://aws.amazon.com/marketplace/pp/prodview-n5llbkfguwale
- Repo grounding: [certification framework](../docs/00-overview/certification-framework.md), [WCA-P](../docs/pam-bastion/wca-p-administrator.md), [WCP-P](../docs/pam-bastion/wcp-p-professional.md), [WCE-P](../docs/pam-bastion/wce-p-expert.md), [bastion-architecture](../deep-dives/bastion-architecture.md)
