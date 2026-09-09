# 01 — Lab Objectives

## Project Goal

The goal of this project is to build an isolated Security Operations Center (SOC) homelab for practicing endpoint monitoring, SIEM analysis, security event investigation, and defensive cybersecurity workflows.

The environment is designed to simulate a small enterprise monitoring setup using a Windows endpoint, an attacker/testing machine, and a Wazuh SIEM server.

## Primary Objectives

- Build an isolated virtual cybersecurity lab using VirtualBox.
- Configure multiple virtual machines on the same internal network.
- Deploy a Windows 10 endpoint for security monitoring.
- Install and configure Sysmon for enhanced Windows endpoint telemetry.
- Install and configure the Wazuh Agent on the Windows endpoint.
- Deploy Wazuh as the centralized SIEM platform.
- Forward Windows Security and Sysmon events to Wazuh.
- Verify end-to-end telemetry ingestion.
- Search and investigate endpoint events through the Wazuh Dashboard.
- Capture evidence of successful monitoring and validation.
- Document the complete lab architecture, configuration, testing, and troubleshooting process.

## SOC Skills Practiced

This project provides hands-on practice with:

- Security Information and Event Management (SIEM)
- Endpoint telemetry
- Windows Event Logs
- Sysmon
- Log collection and forwarding
- Event investigation
- Security monitoring
- Network segmentation
- Troubleshooting telemetry pipelines
- Security documentation

## Lab Use Case

The completed homelab serves as the foundation for additional SOC analyst projects, including:

- Brute-force attack detection
- Suspicious PowerShell investigation
- Process execution analysis
- Phishing investigation
- Threat hunting
- MITRE ATT&CK mapping
- Incident investigation

## Expected Outcome

At the end of Project 1, the following telemetry pipeline should be operational:

```text
Windows Activity
      ↓
Sysmon / Windows Event Logs
      ↓
Wazuh Agent
      ↓
Wazuh Server
      ↓
Wazuh Dashboard
      ↓
SOC Investigation
