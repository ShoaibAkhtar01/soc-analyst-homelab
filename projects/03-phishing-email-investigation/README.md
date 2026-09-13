# Project 3 — Phishing Email Detection & Incident Investigation

## Overview

This project demonstrates a controlled phishing-email detection and investigation workflow in an isolated SOC homelab.

A simulated suspicious email was delivered to a Windows 10 victim system using Swaks and received through Mailpit. A custom Python email analyzer inspected the message for phishing indicators, generated a Windows Application event, and forwarded that telemetry into Wazuh.

A custom Wazuh detection rule generated an alert mapped to MITRE ATT&CK T1566.002 — Spearphishing Link. The incident was then investigated using email headers, IOC analysis, Sysmon telemetry, browser evidence, and SIEM correlation.

The objective was not only to generate an alert, but to determine whether the email resulted in successful user interaction or endpoint compromise.

---

## Lab Environment

- Kali Linux — attacker / simulation system
- Windows 10 — monitored victim endpoint
- Wazuh — SIEM and alerting
- Sysmon — endpoint telemetry
- Mailpit — local SMTP testing / email receiver
- Swaks — controlled email generation
- Python — phishing email analysis
- PowerShell — Windows event generation and investigation

Lab network:

```text
Kali Linux      192.168.100.3
Windows 10      192.168.100.4
Wazuh Server    192.168.100.5
```

## Detection Workflow

```
Controlled suspicious email
        ↓
Windows Mailpit receiver
        ↓
Python email analyzer
        ↓
Windows Application Event ID 3101
        ↓
Wazuh Agent
        ↓
Wazuh built-in Windows warning rule 18102
        ↓
Custom Wazuh Rule 100301
        ↓
MITRE ATT&CK T1566.002
        ↓
SOC investigation and impact assessment
```
## Simulated Phishing Indicators
The controlled message contained several suspicious characteristics:
```
Urgency language
Credential verification request
Login-oriented wording
Embedded URL
Sender / Reply-To domain mismatch
Threat of account suspension
```
Example indicators:
```
From:
it-support@company.local

Reply-To:
support@security-help.local

Subject:
URGENT: Verify your account immediately

URL:
http://security-check.example/login
```
The .example domain and .local addresses were intentionally used as safe lab-only indicators.

## Python Email Analyzer
The custom analyzer:
```
Retrieves messages from the Mailpit API
Extracts sender, Reply-To, subject, URLs, and attachment count
Scores phishing indicators
Assigns verdict and severity
Generates Windows Application Event ID 3101 for suspicious messages
```
Final suspicious-email result:
```
Score       : 8
Verdict     : suspicious
Severity    : high
```
Source:
```scripts/email_analyzer.py``` 
## Windows Event Generation
Suspicious detections were written to the Windows Application log using:
```
Provider: SOC-EmailSecurity
Event ID: 3101
Level: Warning
```
The event contained JSON-formatted investigation context including:
```
sender
Reply-To
subject
URL
score
verdict
severity
detection reasons
```
This provided a structured telemetry source for Wazuh.

## Wazuh Detection Engineering
A custom Wazuh rule was created:
```
<rule id="100301" level="10">
  <if_sid>18102</if_sid>

  <id>^3101$</id>
  <extra_data>^SOC-EmailSecurity$</extra_data>

  <description>
    Potential phishing email detected by SOC email analyzer
  </description>

  <mitre>
    <id>T1566.002</id>
  </mitre>
</rule>
```
The rule builds on Wazuh built-in Rule 18102, which handles decoded Windows warning events.
Detection chain:
```
Windows Event 3101
→ Wazuh Rule 18102
→ Custom Rule 100301
→ Level 10 alert
→ MITRE ATT&CK T1566.002
```
Source:
```rules/project3_email_rules.xml```
Evidence:


## Email Header Investigation
The raw message headers were reviewed to verify message provenance and identify suspicious properties.
Key observations:
```
The visible sender claimed to be internal IT support.
The Reply-To address used a different domain.
The Received header showed the controlled lab source at 192.168.100.3.
The X-Mailer header identified Swaks as the simulation tool.
SPF, DKIM, and DMARC results were not available in this lab scenario.
```
Evidence:

## IOC Analysis
Indicators were classified before enrichment.
Because the environment used reserved and private lab indicators, they were not submitted to external reputation services as if they were real malicious infrastructure.
Examples:
```
security-check.example
Reserved simulation domain

192.168.100.3
Private Kali lab IP

support@security-help.local
Lab-only Reply-To address
```
Investigation notes:
```investigation/ioc-analysis.txt```

## Endpoint Investigation

sysmon telemetry was reviewed for evidence of interaction with the phishing URL.

A Sysmon Event ID 22 showed:
```
Process:
msedge.exe

QueryName:
security-check.example

QueryStatus:
9003

QueryResults:
-
```
This confirmed browser-associated DNS activity.
However:
```
DNS resolution failed.
No matching Edge browser-history navigation entry was found.
No matching Sysmon Event ID 3 Edge network connection was found in the investigated time window.
No credential submission was observed.
No malicious execution was observed.
```
A DNS query alone was not treated as proof that the user clicked the phishing link.

Evidence:

## Incident Timeline

```
03:09:39
Suspicious email delivered to Windows Mailpit.

03:09:41
Email Date header recorded.

03:10:15
Microsoft Edge network service queried security-check.example.
DNS resolution failed.

04:43:29
During later detection-engineering validation,
Windows Application Event ID 3101 was generated.

04:43:32
Wazuh Rule 100301 generated a Level 10 phishing alert.

04:59:45
Additional Event ID 3101 generated during later investigation/testing.
```
The detection-validation events occurred later than the original simulated email activity and are intentionally documented separately.

## Analyst Verdict
```
Classification:
Suspicious phishing-style email

Disposition:
Suspicious — no confirmed successful user interaction

Impact:
Limited observed impact

Credential Compromise:
Not observed

Endpoint Compromise:
Not established
```
The email was considered suspicious because of its urgency, credential-verification language, embedded link, and sender / Reply-To mismatch.
The investigation found browser-associated DNS activity, but DNS resolution failed and no supporting evidence of successful navigation, credential submission, malicious execution, or endpoint compromise was established.

## Recommended Response
Recommended SOC actions include:
```
Remove or quarantine the suspicious message.
Search for other recipients or similar messages.
Block confirmed malicious sender, URL, or domain indicators when applicable.
Review endpoint and account telemetry for follow-on activity.
Verify whether the recipient interacted with the message.
Reset credentials and revoke sessions if credential submission is confirmed.
Isolate the endpoint if evidence of compromise is discovered.
Preserve email, SIEM, and endpoint evidence.
```
## MITRE ATT&CK Mapping

| Technique          | ID        | Tactic         |
| ------------------ | --------- | -------------- |
| Spearphishing Link | T1566.002 | Initial Access |

##
Evidence & Artifacts
 ```
investigation/
├── incident-case-record.txt
└── ioc-analysis.txt

rules/
└── project3_email_rules.xml

scripts/
└── email_analyzer.py

screenshots/
├── 01-phishing-email-analyzer-detection.png
├── 02-wazuh-phishing-alert-detected.png
├── 03-wazuh-phishing-alert-details.png
├── 04-phishing-email-header-analysis.png
└── 05-sysmon-phishing-domain-dns-query.png
```
Full analyst case record:
```investigation/incident-case-record.txt```
## Skills Demonstrated
```
Phishing email triage
Email header analysis
IOC extraction and classification
Python security automation
Windows Event Log integration
Wazuh detection engineering
Custom SIEM rule creation
Sysmon endpoint investigation
Cross-source event correlation
MITRE ATT&CK mapping
Incident timeline reconstruction
Impact assessment
SOC incident documentation
```


