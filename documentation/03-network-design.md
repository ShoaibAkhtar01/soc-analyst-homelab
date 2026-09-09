# Network Design

The lab uses a VirtualBox Internal Network with `192.168.100.0/24`.

| VM | Address | Role |
|---|---|---|
| Kali | `192.168.100.3` | Attacker/testing |
| Windows 10 | `192.168.100.4` | Endpoint |
| Wazuh | `192.168.100.5` | SIEM |

The network is isolated from the host network for controlled testing.
