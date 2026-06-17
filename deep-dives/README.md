# Deep dives — WALLIX Bastion internals

Detailed technical study of WALLIX Bastion and Access Manager, going beyond the
[product portfolio overview](../docs/00-overview/product-portfolio.md). This is the
core material for the **WCP-P** and **WCE-P** certifications. Sourced from the official
WALLIX Bastion Administration Guide (served v12.3.2), Access Manager Guide (v5.2.4.0),
and Deployment Guide (v12.0.2).

| Page | Focus | Cert level |
|------|-------|-----------|
| [Bastion architecture](bastion-architecture.md) | Proxy/gateway model, front-leg vs back-leg, internal services, deployment | WCP-P |
| [Bastion data model](bastion-data-model.md) | The ACL objects (user/target/authorization…) with a worked example | WCP-P |
| [Session management](session-management.md) | Proxies & sub-protocols, recording, OCR, Session Probe, monitoring, approval | WCP-P |
| [Secrets & password management](secrets-and-password-management.md) | Vault, check-out/check-in, rotation, plugins, external vaults, AAPM/WAAPM | WCP-P |
| [Authentication & Access Manager](authentication-and-access-manager.md) | Auth methods (LDAP/Kerberos/SAML/OIDC/X.509/2FA), WAM as HTML5 gateway | WCP-P / WCE-P |
| [High availability & DR](high-availability-and-dr.md) | DB replication over autossh, Master/Slave & Master/Master, failover | WCE-P |
| [REST API & automation](rest-api-and-automation.md) | API auth, resources, curl examples, IaC, CI/CD secret retrieval | WCE-P |
| [Troubleshooting & logs](troubleshooting-and-logs.md) | Log locations, common issues, plugin debugging, SIEM, support process | WCE-P |

💡 New to the concepts? Read [foundations](../foundations/README.md) and
[prerequisites](../prerequisites/README.md) first. Practice with
[hands-on exercises](../labs/hands-on-exercises.md).
