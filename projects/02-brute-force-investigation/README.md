
# Project 2 — SSH Brute-Force Detection & Investigation

## Overview

This project demonstrates a controlled SSH password-guessing simulation against a Windows 10 endpoint inside an isolated SOC homelab.

The objective was to generate repeated authentication failures, detect the activity using Windows Security logs and Wazuh, correlate multiple log sources, identify the source of the authentication attempts, and determine whether the targeted account was successfully accessed.

The investigation was performed from the perspective of an entry-level SOC analyst, focusing on detection, log analysis, event correlation, incident investigation, and evidence-based conclusions.

## Lab Environment

| System | Role | IP Address |
|---|---|---|
| Kali Linux | Controlled attack/test machine | `192.168.100.3` |
| Windows 10 | Monitored endpoint | `192.168.100.4` |
| Wazuh Server | SIEM / log analysis | `192.168.100.5` |

### Security Tools and Telemetry

- Wazuh SIEM
- Wazuh Agent
- Windows Security Event Logs
- Windows OpenSSH
- Sysmon
- Kali Linux
- Hydra
- VirtualBox Internal Network

## Investigation Objective

The investigation was designed to answer four primary questions:

1. Were repeated authentication failures generated on the Windows endpoint?
2. Were those authentication events visible and detectable in Wazuh?
3. Could the source of the authentication attempts be identified through log correlation?
4. Did the observed password-guessing activity result in a successful SSH password authentication?
