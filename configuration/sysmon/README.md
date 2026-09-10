# Sysmon Configuration

## Purpose

Sysmon is installed on the Windows 10 monitored endpoint (`192.168.100.4`) to provide enhanced endpoint telemetry for the SOC Analyst Homelab.

Sysmon records system activity in the following Windows Event Log channel:

```text
Microsoft-Windows-Sysmon/Operational
```
## Telemetry Used
For Project 1, Sysmon process creation telemetry was used to validate endpoint monitoring.
```
Sysmon Event ID 1 — Process Creation
Benign test process: notepad.exe
Events verified locally through Windows Event Viewer
Sysmon telemetry successfully forwarded to Wazuh
```
## Collection Flow
```
Windows Activity
      ↓
Sysmon
      ↓
Sysmon Operational Log
      ↓
Wazuh Agent
      ↓
Wazuh SIEM
```
## Configuration Note
The complete Sysmon configuration file is not included in this repository because this project documents only the configuration and telemetry that were validated in the lab.

Future detection projects may expand the Sysmon configuration as additional telemetry requirements are introduced.
## Documentation
``` See documentation/06-sysmon-deployment.md for the deployment and validation process.```

