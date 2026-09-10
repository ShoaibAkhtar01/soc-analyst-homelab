# Wazuh Configuration

## Purpose

Wazuh is used as the centralized SIEM platform for the SOC Analyst Homelab.

The Windows 10 endpoint (`192.168.100.4`) runs the Wazuh Agent and forwards configured Windows and Sysmon telemetry to the Wazuh environment at `192.168.100.5`.

## Sysmon Event Collection

The Windows Wazuh Agent is configured to collect the Sysmon Operational event channel:

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```
This configuration is located within the Windows Wazuh Agent ossec.conf file.

## Agent Service
After configuration changes, the Wazuh Agent can be restarted from an elevated PowerShell session:
```
Restart-Service -Name Wazuh
```
The service status can be verified using:
``` Get-Service -Name Wazuh ```

## Telemetry Flow
```
Windows Event Logs / Sysmon
          ↓
      Wazuh Agent
          ↓
      Wazuh Server
          ↓
      Wazuh Indexer
          ↓
     Wazuh Dashboard
```
## Documentation
See documentation/07-wazuh-agent.md for detailed Wazuh Agent configuration and validation.

