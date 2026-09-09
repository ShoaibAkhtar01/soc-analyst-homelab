##  Lab Architecture

The SOC Analyst Homelab is designed to simulate a small enterprise security monitoring environment where attacks are generated from an isolated Kali Linux machine and monitored through a Windows endpoint using Sysmon and Wazuh.

### Architecture Diagram

![SOC Homelab Architecture](./Architecture-Diagram.png)

### Network Diagram

![SOC Homelab Network Diagram](./Network-Diagram.png)

The environment separates the attacker, endpoint, and SIEM components while allowing security telemetry to flow from the Windows endpoint to the Wazuh server for centralized monitoring and investigation.

## 🖥️ Lab Environment

The SOC Analyst Homelab consists of isolated virtual machines and security monitoring components designed to simulate a real-world SOC environment.

| Component        | Role                        | Security Tools                     |
| ---------------- | --------------------------- | ---------------------------------- |
| **Kali Linux**   | Attacker / Security Testing | Nmap, Hydra, Wireshark, Burp Suite |
| **Windows 10**   | Monitored Endpoint / Victim | Sysmon, Wazuh Agent                |
| **Wazuh Server** | SIEM / Security Monitoring  | Wazuh Manager, Wazuh Dashboard     |
| **Sysmon**       | Endpoint Telemetry          | Microsoft Sysinternals Sysmon      |
| **Wazuh Agent**  | Log Collection & Forwarding | Wazuh Agent                        |

### Component Roles

#### 🔴 Kali Linux — Attacker

Kali Linux is used to simulate controlled attacks against the Windows endpoint. It is used for reconnaissance, vulnerability testing, authentication attacks, and other security testing activities.

#### 🪟 Windows 10 — Monitored Endpoint

The Windows 10 machine represents an enterprise endpoint being monitored by the SOC. Windows Security logs and Sysmon telemetry provide visibility into authentication events, process execution, network activity, and other endpoint activity.

#### 🛡️ Sysmon — Endpoint Telemetry

Sysmon provides detailed system-level telemetry from the Windows endpoint, including process creation, network connections, and other security-relevant events.

#### 📊 Wazuh Server — SIEM

The Wazuh Server provides centralized security monitoring and analysis. It receives telemetry from the monitored endpoint, processes events, generates alerts, and provides dashboards for investigation.

#### 📡 Wazuh Agent — Log Collection

The Wazuh Agent runs on the Windows endpoint and collects relevant security and system events before forwarding them to the Wazuh Server for centralized analysis.

