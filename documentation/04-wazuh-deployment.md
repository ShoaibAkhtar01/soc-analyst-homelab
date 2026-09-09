# 04 — Wazuh Deployment

## 1. Overview

Wazuh is used as the centralized Security Information and Event Management (SIEM) platform in the SOC Analyst Homelab.

The Wazuh environment receives security telemetry from the monitored Windows 10 endpoint and provides a centralized interface for security monitoring and investigation.

The Wazuh server is configured with the following lab address:

`192.168.100.5`

---

## 2. Role in the Homelab

The Wazuh platform provides the central monitoring layer of the SOC environment.

Its primary functions in this project are:

- Receive telemetry from the Windows endpoint.
- Monitor the status of the Windows Wazuh Agent.
- Process collected security events.
- Store and index security telemetry.
- Provide event searching and investigation capabilities.
- Display security information through the Wazuh Dashboard.

---

## 3. Wazuh Components

The Wazuh deployment consists of the primary Wazuh components:

### Wazuh Manager

The Wazuh Manager receives and analyzes security telemetry collected from monitored endpoints.

### Wazuh Indexer

The Wazuh Indexer stores and indexes security data so that events can be searched and analyzed.

### Wazuh Dashboard

The Wazuh Dashboard provides the web interface used by the SOC analyst to:

- View monitored endpoints.
- Search security events.
- Analyze Windows telemetry.
- Investigate security activity.
- Review endpoint status and security information.

---

## 4. Lab Configuration

| Setting | Value |
|---|---|
| Platform | Wazuh |
| Role | SIEM / Security Monitoring |
| IP Address | `192.168.100.5` |
| Network | VirtualBox Internal Network |
| Lab Network | `192.168.100.0/24` |
| Monitored Endpoint | Windows 10 |
| Endpoint IP | `192.168.100.4` |

The Wazuh server and Windows endpoint communicate through the isolated VirtualBox lab network.

---

## 5. Wazuh Dashboard Validation

After deployment, the Wazuh Dashboard was accessed through the lab environment to verify that the SIEM interface was operational.

Evidence:

![Wazuh Dashboard](../screenshots/01b-wazuh-dashboard.png)

Successful dashboard access confirms that the Wazuh web interface is available for monitoring and investigation.

---

## 6. Windows Endpoint Registration

The Windows 10 endpoint was enrolled with the Wazuh environment using the Wazuh Agent.

The monitored endpoint uses:

`192.168.100.4`

After registration, the endpoint was verified in the Wazuh Dashboard.

Evidence:

![Windows Wazuh Agent Active](../screenshots/02-windows-agent-active.png)

The active agent status confirms communication between the Windows endpoint and the Wazuh server.

---

## 7. Windows Event Collection

The Windows endpoint generates security telemetry through Windows Event Logs.

The Wazuh Agent collects configured Windows events and forwards them to the Wazuh environment.

The basic collection path is:

```text
Windows Event Logs
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
Windows event ingestion was validated through the Wazuh interface.

```
## 8.  Sysmon Integration

Sysmon is installed on the Windows endpoint to provide enhanced endpoint telemetry.

The Wazuh Agent is configured to collect the Sysmon Operational event channel:
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
The monitored event channel is:
Microsoft-Windows-Sysmon/Operational

## 9. Sysmon Telemetry Validation
After configuring Sysmon collection, benign process activity was generated on the Windows endpoint.

The resulting Sysmon telemetry was verified in Wazuh.

Evidence:

This confirms that Sysmon telemetry can travel through the complete monitoring pipeline:
Windows Process Activity
        |
        v
      Sysmon
        |
        v
Windows Event Log
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

 ## 10. Deployment Validation

The Wazuh deployment was considered operational after successfully confirming:

The Wazuh Dashboard was accessible.
The Windows endpoint was registered.
The Wazuh Agent reported an active status.
Windows security telemetry was generated on the endpoint.
Windows events were visible in Wazuh.
Sysmon generated endpoint telemetry.
Sysmon telemetry was successfully searchable in Wazuh.

These validation checks demonstrate that the SIEM environment is capable of receiving and presenting endpoint security telemetry for SOC analysis.

