
# Wazuh Agent Connectivity & Telemetry Recovery

## Overview

During the SOC homelab network migration, the Windows endpoint became
disconnected from the Wazuh Manager and fresh Sysmon telemetry was not
initially visible in the Wazuh Dashboard.

The issue was investigated systematically across the network, endpoint,
Wazuh agent, manager, Sysmon, and SIEM ingestion layers.

---

## Environment

| Component | Configuration |
|---|---|
| Windows 10 Victim | 10.10.10.10 |
| Wazuh Server | 10.10.10.20 |
| Wazuh Agent ID | 003 |
| Agent Name | victim |
| SIEM | Wazuh |
| Endpoint Telemetry | Sysmon |
| Wazuh Agent | v4.14.7 |

---

## Problem

The Wazuh Dashboard initially showed the Windows endpoint as
**Disconnected**.

Although the Windows Wazuh service and Sysmon service were running,
fresh endpoint telemetry was not appearing correctly in the SIEM.

---

## Investigation

### 1. Network Connectivity

Verified connectivity between the Windows endpoint and the Wazuh
infrastructure.

The endpoint also had working DNS and Internet connectivity.

### 2. Wazuh Services

Verified that the Wazuh Dashboard and associated services were running.

The Wazuh Manager was listening for agent communication on TCP port 1514.

### 3. Windows Agent

Verified the Wazuh agent service:

```powershell
Get-Service WazuhSvc
```
### 4. Sysmon
Verified the Sysmon service and confirmed that Sysmon events were being
generated locally.
```
Get-Service Sysmon64

Get-WinEvent `
  -LogName "Microsoft-Windows-Sysmon/Operational" `
  -MaxEvents 5
```
### 5. Event Channel Configuration
Verified that the Wazuh agent was monitoring:
``` Microsoft-Windows-Sysmon/Operational ```
### 6. Agent Connection
The Wazuh agent logs eventually confirmed a successful connection to:
``` 10.10.10.20:1514/tcp ```
The Wazuh Manager subsequently reported:
```
Agent ID: 003
Name: victim
Status: Active
```
### Detection Validation
After restoring connectivity, new endpoint activity was generated.

Wazuh successfully received and analyzed fresh Sysmon telemetry.

Observed detections included:
```
PowerShell process activity
Suspicious Windows command shell execution
PowerShell-related Sysmon events
Windows vulnerability/CVE alerts
```
The Wazuh Dashboard displayed fresh alerts associated with:
```
agent.id   : 003
agent.name : victim
agent.ip   : 10.10.10.10
```
This confirmed successful end-to-end telemetry:
```
Windows Endpoint
      ↓
Sysmon
      ↓
Wazuh Agent
      ↓
Wazuh Manager
      ↓
Detection Rules
      ↓
Wazuh Indexer
      ↓
Wazuh Dashboard
```
### Result
The Windows endpoint successfully returned to an active state and fresh
Sysmon events were visible in the Wazuh Dashboard.

This troubleshooting exercise demonstrated practical experience with:
```
SIEM troubleshooting
Endpoint telemetry validation
Wazuh agent diagnostics
Windows event-log analysis
Sysmon
Network connectivity testing
Log ingestion validation
Detection verification
```
