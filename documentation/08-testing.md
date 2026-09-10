# 08 — Testing and Validation

## 1. Overview

After deploying the SOC Analyst Homelab, a series of validation tests were performed to confirm that the network, endpoint monitoring components, Windows telemetry, Sysmon telemetry, Wazuh Agent, and Wazuh SIEM were functioning correctly.

The objective was to validate the complete telemetry pipeline:

```text
Windows Activity
       |
       v
Sysmon / Windows Event Logs
       |
       v
Wazuh Agent
       |
       v
Wazuh Server
       |
       v
Wazuh Indexer
       |
       v
Wazuh Dashboard
       |
       v
SOC Investigation
```
## 2. Test Environment
```
| System       | Role               | IP Address      |
| ------------ | ------------------ | --------------- |
| Kali Linux   | Attacker / Testing | `192.168.100.3` |
| Windows 10   | Monitored Endpoint | `192.168.100.4` |
| Wazuh Server | SIEM               | `192.168.100.5` |
```
All systems communicate through the isolated VirtualBox Internal Network:
``` 192.168.100.0/24 ```

## 3. Test 1 — Network Connectivity
Objective

Confirm that the virtual machines can communicate through the internal lab network.

Systems Tested
```
Kali Linux  <----> Windows 10
Windows 10  <----> Wazuh
Kali Linux  <----> Wazuh
```
Result

PASS

The three virtual machines were able to communicate across the configured internal network.

This confirmed that the network layer was operational before endpoint telemetry testing was performed.

## 4. Test 2 — Wazuh Dashboard Access
Objective

Confirm that the Wazuh Dashboard is accessible and available for SOC monitoring.

Validation

The Wazuh web interface was accessed using the Wazuh server at:
``` 192.168.100.5 ```
Result

PASS

The Wazuh Dashboard was successfully accessed.

Evidence is available in:
```
screenshots/01-wazuh-dashboard-access.png
screenshots/01b-wazuh-dashboard.png
```
## 5. Test 3 — Windows Wazuh Agent Status
Objective

Confirm that the Windows endpoint is successfully registered with the Wazuh server and actively reporting.

Endpoint
```
Windows 10
192.168.100.4
```

Validation

The endpoint was checked through the Wazuh Dashboard.

Result

PASS

The Windows endpoint appeared as an active Wazuh Agent.

Evidence:
``` screenshots/02-windows-agent-active.png```
This confirmed successful endpoint-to-Wazuh communication.

## 6. Test 4 — Sysmon Local Event Generation

Objective

Confirm that Sysmon is installed correctly and generating endpoint telemetry.

Validation Location
```
Event Viewer
→ Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```
Result

PASS

Sysmon Operational events were successfully generated on the Windows endpoint.

Evidence:
``` screenshots/03-sysmon-operational-events.png ```
This confirmed that Sysmon itself was functioning before testing SIEM ingestion.
## 7. Test 5 — Windows Security Events
Objective

Confirm that Windows Security auditing is generating security events on the monitored endpoint.

Validation

Windows Event Viewer was used to inspect the Security event channel.

Result

PASS

Windows Security events were available on the monitored Windows endpoint.

Evidence:
``` screenshots/04-windows-security-events.png ```
## 8. Test 6 — Windows Events in Wazuh
Objective

Confirm that Windows endpoint telemetry is successfully received by the Wazuh environment.

Validation

Windows events generated on the endpoint were searched through Wazuh.

Result

PASS

Windows telemetry was successfully visible in Wazuh.

Evidence:
``` screenshots/05-wazuh-windows-events.png ```
This confirmed the following collection path:
```
Windows Event
      |
      v
Wazuh Agent
      |
      v
Wazuh Server
      |
      v
Wazuh Dashboard
```
## 9. Test 7 — Sysmon Process Telemetry
Objective

Confirm end-to-end Sysmon telemetry ingestion into Wazuh.

Benign Test Activity

A predictable Windows process was generated using:
``` Start-Process notepad.exe ```
The process could then be closed normally or stopped using:
``` Stop-Process -Name notepad```
Local Validation

The newly generated activity was checked in the Sysmon Operational event channel.

The investigation focused on a process creation event associated with:
``` notepad.exe ```
SIEM Validation

Wazuh was searched for the corresponding process telemetry.

Result

PASS

The generated Sysmon process telemetry was successfully visible in Wazuh.

Evidence:
``` screenshots/06-sysmon-telemetry-wazuh.png ```
## 10. Validation Results
```
| Test | Validation                                | Result |
| ---- | ----------------------------------------- | ------ |
| 1    | Internal network connectivity             | PASS   |
| 2    | Wazuh Dashboard access                    | PASS   |
| 3    | Windows Wazuh Agent active                | PASS   |
| 4    | Sysmon events generated locally           | PASS   |
| 5    | Windows Security events available         | PASS   |
| 6    | Windows events visible in Wazuh           | PASS   |
| 7    | Sysmon process telemetry visible in Wazuh | PASS   |
```
Overall Result

7 / 7 validation tests passed.
## 11. Evidence Collection

Evidence captured during the validation process is stored in:
``` screenshots/ ```
The evidence set includes:
```
01-wazuh-dashboard-access.png
01b-wazuh-dashboard.png
02-windows-agent-active.png
03-sysmon-operational-events.png
04-windows-security-events.png
05-wazuh-windows-events.png
06-sysmon-telemetry-wazuh.png
```
The dedicated screenshot documentation explains what each image demonstrates.
## 12. Testing Methodology
A layered testing methodology was used throughout the project.

Rather than troubleshooting the entire telemetry pipeline at once, each component was validated individually.
```
Step 1 — Network connectivity
          |
          v
Step 2 — Wazuh availability
          |
          v
Step 3 — Agent connectivity
          |
          v
Step 4 — Local Windows logging
          |
          v
Step 5 — Local Sysmon logging
          |
          v
Step 6 — Windows telemetry ingestion
          |
          v
Step 7 — Sysmon telemetry ingestion
```
This approach makes it easier to identify which layer is responsible when expected telemetry is missing.

## 13. SOC Analyst Relevance
The testing process demonstrates several practical SOC analyst skills:
```
Validating endpoint visibility
Confirming agent health
Inspecting Windows Event Logs
Working with Sysmon telemetry
Searching SIEM data
Verifying log ingestion
Troubleshooting telemetry gaps
Documenting technical evidence
Validating monitoring coverage
```
## 14. Final Validation
Project 1 successfully demonstrated an operational endpoint-monitoring pipeline using Windows 10, Sysmon, the Wazuh Agent, and Wazuh SIEM.

The final validated workflow is:
```
Endpoint Activity
       |
       v
Windows / Sysmon Telemetry
       |
       v
Wazuh Agent
       |
       v
Wazuh SIEM
       |
       v
Event Search and Analysis
       |
       v
SOC Investigation
```
The environment is now ready to support additional controlled detection and incident-investigation scenarios.


