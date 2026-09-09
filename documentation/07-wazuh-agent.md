# Wazuh Agent

The Windows endpoint uses the Wazuh Agent to forward endpoint telemetry.

Check service status:

```powershell
Get-Service -Name Wazuh
```

Restart after configuration changes:

```powershell
Restart-Service -Name Wazuh
```
