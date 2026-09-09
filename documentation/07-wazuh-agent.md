# 07 — Wazuh Agent Configuration

## 1. Overview

The Wazuh Agent is installed on the Windows 10 endpoint and acts as the telemetry collection component between the monitored endpoint and the Wazuh SIEM.

In this homelab, the agent collects configured Windows event channels, including Sysmon telemetry, and forwards the security data to the Wazuh environment for centralized monitoring and investigation.

---

## 2. Agent Environment

| Setting | Value |
|---|---|
| Endpoint | Windows 10 |
| Endpoint Role | Monitored Endpoint |
| Endpoint IP | `192.168.100.4` |
| Wazuh Server | `192.168.100.5` |
| Network | VirtualBox Internal Network |
| Lab Network | `192.168.100.0/24` |

The basic communication path is:

```text
Windows 10 Endpoint
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
```
## 3. Purpose of the Wazuh Agent
The Wazuh Agent provides endpoint monitoring and telemetry collection capabilities.
Within this project, the agent is used to:
```
Connect the Windows endpoint to the Wazuh environment.
Collect configured Windows Event Logs.
Collect Sysmon Operational events.
Forward endpoint telemetry to the Wazuh server.
Provide endpoint status information in the Wazuh Dashboard.
Support centralized security monitoring and investigation.
```
## 4. Agent Registration
The Windows 10 endpoint was enrolled with the Wazuh environment.
After registration, the endpoint appeared in the Wazuh Dashboard as an active monitored agent.
The endpoint configuration used in the lab is:
```
Endpoint: Windows 10
IP Address: 192.168.100.4
Wazuh Server: 192.168.100.5
```
Successful registration confirms that the Wazuh server recognizes the monitored endpoint.
Evidence is maintained in the repository's screenshots/ directory.

##  5. Agent Service Validation
The Wazuh Agent runs as a Windows service.
An elevated PowerShell session can be used to verify its state:
``` Get-Service -Name Wazuh ```
The expected operational state is:
``` Running ```
A running service confirms that the endpoint agent is active at the operating-system level.

## 6. Restarting the Agent
After changing the Wazuh Agent configuration, the service should be restarted so that the updated configuration is applied.
From an elevated PowerShell session:
``` Restart-Service -Name Wazuh ```
The status can then be verified again:
```  Get-Service -Name Wazuh ```
Expected result:
```Running```

## 7. Windows Event Collection
Windows Event Logs provide telemetry that can be collected by the Wazuh Agent.
The monitoring pipeline is:
```
Windows Activity
       |
       v
Windows Event Logs
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
Windows event ingestion was successfully validated during the project.

## 8. Sysmon Event Collection
Sysmon writes its telemetry to:
```Microsoft-Windows-Sysmon/Operational```
To collect this channel, the Wazuh Agent configuration includes:
```
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```
This configuration instructs the Wazuh Agent to monitor the Sysmon Operational event channel.

## 9. Agent Configuration Location
On the Windows endpoint, the Wazuh Agent configuration is typically located at:
``` C:\Program Files (x86)\ossec-agent\ossec.conf ```
## 10. Sysmon Telemetry Test
After confirming the Sysmon event-channel configuration, a new benign process event was generated.
For example:
``` Start-Process notepad.exe ```
The activity was first verified locally in:
```
Event Viewer
→ Applications and Services Logs
→ Microsoft
→ Windows
→ Sysmon
→ Operational
```
The corresponding Sysmon process creation event was then searched in Wazuh.
Successful discovery confirmed that the agent was collecting and forwarding Sysmon telemetry.

## 11. End-to-End Agent Validation
The Wazuh Agent integration was considered successful after validating:
```
The Wazuh Agent service was running.
The Windows endpoint appeared as active in Wazuh.
Windows events were available locally.
Windows telemetry was visible in Wazuh.
Sysmon events were generated locally.
The Sysmon Operational channel was configured for collection.
New Sysmon process telemetry was visible in Wazuh.
```
The validated flow is:
```
Windows Activity
       |
       v
Windows Event Logs / Sysmon
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
## 12. SOC Analyst Relevance
Understanding endpoint agents is important for SOC analysts because missing telemetry can directly affect detection and investigation capabilities.
A SOC analyst should be able to determine whether:
```
An endpoint is actively reporting.
Expected logs are being generated.
Required event channels are monitored.
Telemetry is reaching the SIEM.
A visibility gap exists.
Agent or configuration problems are affecting detection coverage.
```
This project provides hands-on experience troubleshooting an endpoint-to-SIEM telemetry pipeline.
## Agent Deployment Result
The Wazuh Agent was successfully integrated with the Windows 10 monitored endpoint.

The agent maintained communication with the Wazuh server, collected configured Windows and Sysmon telemetry, and forwarded security events to the centralized Wazuh environment.

This completes the endpoint-to-SIEM collection layer required for SOC monitoring and future detection scenarios.




