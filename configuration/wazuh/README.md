# Wazuh Configuration

Place sanitized Wazuh configuration snippets here.

Important Windows Sysmon collection example:

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

Never publish credentials, API keys, certificates, or private keys.
