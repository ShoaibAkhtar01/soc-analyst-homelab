# 03 — Network Design

## 1. Overview

The SOC Analyst Homelab uses an isolated VirtualBox Internal Network to provide controlled communication between the attacker machine, monitored Windows endpoint, and Wazuh SIEM server.

The lab network is:

`192.168.100.0/24`

The network design allows security-testing activity and endpoint telemetry to remain within the virtual lab environment.

---

## 2. Network Architecture

The environment contains three virtual machines:

| System | Role | IP Address |
|---|---|---|
| Kali Linux | Attacker / Security Testing | `192.168.100.3` |
| Windows 10 | Victim / Monitored Endpoint | `192.168.100.4` |
| Wazuh Server | SIEM / Security Monitoring | `192.168.100.5` |

All three systems are connected to the same VirtualBox Internal Network.

---

## 3. Network Diagram

The following diagram represents the network architecture of the SOC homelab:

![SOC Analyst Homelab Network Diagram](../architecture/Network-Diagram.png)

The network consists of:

- A Kali Linux machine used to generate controlled testing activity.
- A Windows 10 endpoint monitored using Sysmon and the Wazuh Agent.
- A Wazuh server responsible for centralized security monitoring and event analysis.

---

## 4. Network Topology

```text
                    Physical Host
                         |
                    VirtualBox
                         |
                         v
             Internal Network
              192.168.100.0/24
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
     Kali Linux      Windows 10       Wazuh
    192.168.100.3   192.168.100.4   192.168.100.5
      Attacker        Endpoint          SIEM
```
This topology provides direct communication between the three virtual machines while keeping the lab logically separated from the primary host network.

## 5. Communication Flow

Kali Linux → Windows 10

The Kali Linux VM acts as the controlled attacker/testing workstation.
```
Kali Linux
192.168.100.3
      |
      | Controlled testing traffic
      v
Windows 10
192.168.100.4
This communication can be used in future SOC projects to generate activity that can be detected and investigated.
Windows 10 → Wazuh

The Windows endpoint generates security telemetry through Windows Event Logs and Sysmon.
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
192.168.100.5
The Wazuh Agent forwards configured endpoint telemetry to the Wazuh environment for analysis.
```
## 6. Telemetry Flow

The security monitoring pipeline follows this path:
```
Windows Endpoint
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
This provides centralized visibility into security activity occurring on the monitored Windows endpoint.

## 7. Connectivity Validation

Before configuring security monitoring, connectivity between the virtual machines was validated.

The expected communication paths are:
```

Kali    <----> Windows
Windows <----> Wazuh
Kali    <----> Wazuh
```
Successful communication confirms that all three systems are correctly connected to the VirtualBox Internal Network.
## 8. Network Isolation

The lab uses a VirtualBox Internal Network to create a controlled environment for cybersecurity testing.

The purpose of this design is to:
```
Keep lab traffic separated from the primary host network.
Prevent controlled attack simulations from affecting unrelated systems.
Provide predictable IP addressing.
Allow endpoint telemetry to be generated and monitored safely.
Create a repeatable environment for SOC investigations.
```
## 9. Design Benefits

The network architecture provides several benefits for SOC analyst training:
```

Isolation — security-testing traffic remains within the lab.
Visibility — endpoint activity can be monitored through Wazuh.
Repeatability — the same network can be reused for multiple detection scenarios.
Controlled testing — activity can be intentionally generated and investigated.
Centralized monitoring — Windows telemetry is forwarded to the Wazuh SIEM.
Scalability — additional endpoints or security systems can be added later.
```
Network Design Summary
```
VirtualBox Internal Network
192.168.100.0/24

        |
        +---- Kali Linux
        |     192.168.100.3
        |     Attacker / Testing
        |
        +---- Windows 10
        |     192.168.100.4
        |     Monitored Endpoint
        |     Sysmon + Wazuh Agent
        |
        +---- Wazuh Server
              192.168.100.5
              SIEM / Security Monitoring
```
This network provides the isolated foundation required for endpoint monitoring, attack simulation, event collection, and future SOC investigation projects.

