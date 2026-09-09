# 02 — Lab Requirements

## Overview

This document describes the virtualization platform, virtual machines, software components, and network configuration used to build the SOC Analyst Homelab.

## Virtualization Platform

- **VirtualBox**
- Three virtual machines
- VirtualBox Internal Network for isolated VM-to-VM communication

## Virtual Machines

### 1. Kali Linux — Attacker / Test Machine

**Purpose:** Generate controlled security-testing activity against the monitored Windows endpoint.

| Setting | Value |
|---|---|
| Operating System | Kali Linux |
| Role | Attacker / Security Testing |
| IP Address | `192.168.100.3` |
| Network | VirtualBox Internal Network |

Typical uses within the lab:

- Connectivity testing
- Security testing
- Controlled attack simulation
- Enumeration and scanning
- Future SOC detection scenarios

---

### 2. Windows 10 — Monitored Endpoint

**Purpose:** Act as the victim/enterprise endpoint from which security telemetry is collected.

| Setting | Value |
|---|---|
| Operating System | Windows 10 |
| Role | Monitored Endpoint |
| IP Address | `192.168.100.4` |
| Network | VirtualBox Internal Network |

Installed monitoring components:

- **Sysmon**
- **Wazuh Agent**

Telemetry sources include:

- Windows Security Event Logs
- Windows System/Application logs as configured
- Sysmon Operational logs
- Process creation telemetry

---

### 3. Wazuh Server — SIEM

**Purpose:** Centralized security monitoring, log analysis, event searching, and investigation.

| Setting | Value |
|---|---|
| Platform | Wazuh |
| Role | SIEM / Security Monitoring |
| IP Address | `192.168.100.5` |
| Network | VirtualBox Internal Network |

The Wazuh environment provides:

- Wazuh Manager
- Wazuh Indexer
- Wazuh Dashboard

## Network Requirements

The three virtual machines communicate through an isolated VirtualBox Internal Network.

```text
Network: 192.168.100.0/24

Kali Linux     192.168.100.3
Windows 10     192.168.100.4
Wazuh Server   192.168.100.5
This design allows the lab systems to communicate with each other while keeping security-testing traffic separated from the primary host network.

##Endpoint Monitoring Requirements

The Windows endpoint requires:

#1 Sysmon

Sysmon provides enhanced Windows telemetry such as process creation events and other endpoint activity.

#2 Wazuh Agent

The Wazuh Agent collects configured Windows event channels and forwards security telemetry to the Wazuh server.

## Validation Requirements

The environment is considered operational when:

All three VMs can communicate across the internal network.
The Wazuh Dashboard is accessible.
The Windows endpoint appears as an active Wazuh Agent.
Sysmon generates events in Windows Event Viewer.
Windows Security events are available.
Windows events are received by Wazuh.
Sysmon telemetry generated on the Windows endpoint is searchable in Wazuh.
Security Considerations

The lab is intended only for authorized cybersecurity training and defensive-security experimentation.
