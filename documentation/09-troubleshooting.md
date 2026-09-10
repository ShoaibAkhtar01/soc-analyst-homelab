# 09 — Troubleshooting

## Issue — Sysmon Telemetry Not Visible in Wazuh

During validation, Sysmon events were successfully generated on the Windows 10 endpoint, but the expected Sysmon telemetry was initially not visible in Wazuh.

### Investigation

The following checks were performed:

1. Confirmed Sysmon was generating events locally in:

```text
Microsoft-Windows-Sysmon/Operational
```
2.Confirmed Sysmon Process Creation events (Event ID 1) existed in Windows Event Viewer.
3.Verified that the Wazuh Agent was running and the Windows endpoint appeared as active in Wazuh.
4.Verified the Wazuh Agent configuration included the Sysmon event channel:
```
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```
5.Restarted the Wazuh Agent:
``` Restart-Service -Name Wazuh ```
6.Generated new benign process activity using notepad.exe and searched for the new telemetry in Wazuh.
Result

The new Sysmon process telemetry became visible in Wazuh, confirming successful end-to-end collection:
```
Windows Activity
      ↓
Sysmon
      ↓
Wazuh Agent
      ↓
Wazuh Server
      ↓
Wazuh Dashboard
```
#Key Learning

Troubleshooting should validate each layer separately: first confirm the event exists locally, then verify agent configuration and connectivity, and finally confirm SIEM ingestion.
