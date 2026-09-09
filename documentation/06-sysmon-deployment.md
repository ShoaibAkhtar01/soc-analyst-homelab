# 06 — Sysmon Deployment

## 1. Overview

Sysmon (System Monitor) is deployed on the Windows 10 endpoint to provide enhanced endpoint telemetry for the SOC Analyst Homelab.

Sysmon records detailed system activity into the Windows Event Log, allowing security analysts to investigate endpoint behavior that may not be sufficiently visible through standard Windows logging alone.

In this project, Sysmon telemetry is collected by the Wazuh Agent and forwarded to the Wazuh SIEM for centralized monitoring and investigation.

---

## 2. Sysmon Role in the Lab

Sysmon is installed on:

| Setting | Value |
|---|---|
| Endpoint | Windows 10 |
| Endpoint IP | `192.168.100.4` |
| Role | Monitored Endpoint |
| SIEM | Wazuh |
| Wazuh Server | `192.168.100.5` |

The telemetry path is:

```text
Windows Activity
       |
       v
     Sysmon
       |
       v
Sysmon Operational Log
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
## 3. Sysmon Event Channel
Sysmon writes its events to the following Windows Event Log channel:
```Microsoft-Windows-Sysmon/Operational```
This channel can be viewed through Windows Event Viewer:
```
Event Viewer
   |
   v
Applications and Services Logs
   |
   v
Microsoft
   |
   v
Windows
   |
   v
Sysmon
   |
   v
Operational
```
This location was used during the project to verify that Sysmon was generating endpoint telemetry locally.

## 4. Process Creation Telemetry

One of the important Sysmon event types used during this project was process creation.
Sysmon Event ID 1 represents process creation activity.
Process creation telemetry can provide useful information such as:
```
Process image
Command line
Process ID
Parent process information
User context
Process creation time
Process hashes when configured
```
This type of telemetry is valuable to SOC analysts when investigating suspicious execution.

## 5. Local Sysmon Validation

Before attempting to locate Sysmon telemetry in Wazuh, Sysmon functionality was validated directly on the Windows endpoint.
The validation process included:
```
Open Windows Event Viewer.
Navigate to Microsoft-Windows-Sysmon/Operational.
Confirm that Sysmon events are being generated.
Locate process creation events.
Verify recent event timestamps and process information.
```
Evidence for this validation is maintained in the repository's screenshots/ directory.

## 6. Wazuh Sysmon Collection
The Wazuh Agent must monitor the Sysmon Operational event channel for Sysmon events to reach the SIEM.
The Windows Wazuh Agent configuration includes:
```
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```
This configuration instructs the Wazuh Agent to collect events from the Sysmon Operational channel.

## 7. Restarting the Wazuh Agent

After confirming or modifying the event-channel configuration, the Wazuh Agent can be restarted from an elevated PowerShell session.
``` Restart-Service -Name Wazuh ```
The service status can then be checked using:
``` Get-Service -Name Wazuh ```
The expected state is:
``` Running ```
Restarting the agent ensures that relevant configuration changes are applied before new validation activity is generated.

## 8. Generating Benign Test Activity
A benign Windows process was used to validate the Sysmon telemetry pipeline.
For example:
``` Start-Process notepad.exe ```
After allowing the activity to be recorded, Notepad can be closed normally or stopped using:
``` Stop-Process -Name notepad ```
This provides predictable process activity that can be searched locally and in Wazuh.

## 9. Event Validation

After generating the benign process activity, the Sysmon Operational log was checked for a new process creation event.
```
Event ID: 1
Process: notepad.exe
Provider: Microsoft-Windows-Sysmon
```
The timestamp of the event was also checked to ensure that the event corresponded to the newly generated test activity.

## 10. Wazuh Validation
After confirming that Sysmon generated the event locally, Wazuh was searched for the corresponding telemetry.
Useful search indicators included:
``` notepad.exe ```
and Sysmon-related fields such as:
```win.system.providerName
win.system.eventID
win.eventdata.image
```
Successful discovery of the process telemetry in Wazuh confirmed that Sysmon events were being forwarded through the Wazuh Agent.
Evidence is maintained in the repository's screenshots/ directory.

## 11. End-to-End Telemetry Validation
```
notepad.exe
     |
     v
Sysmon Event ID 1
     |
     v
Microsoft-Windows-Sysmon/Operational
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
This demonstrates that endpoint process activity can be collected and analyzed through the centralized SIEM environment.

## 12. SOC Analyst Relevance
Sysmon telemetry is useful in SOC investigations because it provides detailed endpoint visibility.
Process creation telemetry can help analysts investigate:
```Suspicious executable launches
Command-line activity
Parent-child process relationships
PowerShell execution
Potential malware execution
Living-off-the-land activity
Unexpected applications
Attack timelines
```
The Sysmon integration created in Project 1 will therefore support more advanced detection and investigation scenarios in future projects.







