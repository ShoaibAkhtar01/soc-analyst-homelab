# SOC Analyst Homelab

A hands-on virtualized SOC environment for security monitoring, Windows endpoint telemetry, SIEM analysis, and incident investigation.

## Project 1 Status
**Completed:** end-to-end Windows telemetry validation.

```text
Windows activity -> Sysmon -> Windows Event Logs -> Wazuh Agent
-> Wazuh Server/Indexer -> Wazuh Dashboard -> SOC investigation
```

## Lab Architecture

```text
VirtualBox Internal Network: 192.168.100.0/24

Kali Linux       Windows 10              Wazuh
192.168.100.3    192.168.100.4           192.168.100.5
Attacker         Endpoint                SIEM
                 |                       ^
                 | Sysmon + Agent         |
                 +---- telemetry --------+
```

## Components

| Component | Role | IP |
|---|---|---|
| Kali Linux | Security testing workstation | `192.168.100.3` |
| Windows 10 | Monitored endpoint | `192.168.100.4` |
| Wazuh | SIEM / monitoring server | `192.168.100.5` |
| Sysmon | Windows endpoint telemetry | Windows |
| Wazuh Agent | Endpoint log forwarding | Windows |

## Validation Evidence

Six validation checks were completed:

1. Wazuh Dashboard accessible
2. Windows Agent active
3. Sysmon events visible locally
4. Windows Security events visible
5. Windows events visible in Wazuh
6. Sysmon `notepad.exe` telemetry visible in Wazuh

Evidence files:

```text
screenshots/
├── 01-wazuh-dashboard.png
├── 02-windows-agent-active.png
├── 03-sysmon-events.png
├── 04-windows-security-events.png
├── 05-wazuh-windows-events.png
└── 06-wazuh-sysmon-notepad-event.png
```

## Documentation

- [Objectives](documentation/01-lab-objectives.md)
- [Requirements](documentation/02-requirements.md)
- [Network Design](documentation/03-network-design.md)
- [Wazuh Deployment](documentation/04-wazuh-deployment.md)
- [Windows Endpoint](documentation/05-windows-endpoint.md)
- [Sysmon Deployment](documentation/06-sysmon-deployment.md)
- [Wazuh Agent](documentation/07-wazuh-agent.md)
- [Testing](documentation/08-testing.md)
- [Troubleshooting](documentation/09-troubleshooting.md)

## Security

Do not commit passwords, API keys, tokens, private keys, VM disk images, raw sensitive logs, or personal information. Publish only sanitized configuration and evidence.

## Future Projects

- Project 2: Brute-force detection
- Project 3: PowerShell / suspicious execution detection
- Project 4: Phishing investigation
- Project 5: Threat hunting and MITRE ATT&CK mapping

## Disclaimer

For educational, defensive-security, and authorized lab testing only.

## Author

Shoaib Akhtar
