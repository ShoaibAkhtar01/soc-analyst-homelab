# Sysmon Deployment

Sysmon provides detailed Windows endpoint telemetry, including process creation.

The Wazuh Agent collects the Sysmon Operational channel:

```xml
<localfile>
  <location>Microsoft-Windows-Sysmon/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
```

After configuration changes, restart the agent and generate a new benign event for validation.

A benign `notepad.exe` process was used to validate process telemetry.
