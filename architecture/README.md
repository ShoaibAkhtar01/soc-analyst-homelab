##  Lab Architecture

The SOC Analyst Homelab is designed to simulate a small enterprise security monitoring environment where attacks are generated from an isolated Kali Linux machine and monitored through a Windows endpoint using Sysmon and Wazuh.

### Architecture Diagram

![SOC Homelab Architecture](./Architecture-Diagram.png)

### Network Diagram

![SOC Homelab Network Diagram](./Network-Diagram.png)

The environment separates the attacker, endpoint, and SIEM components while allowing security telemetry to flow from the Windows endpoint to the Wazuh server for centralized monitoring and investigation.
