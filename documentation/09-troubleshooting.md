# Troubleshooting

When Sysmon events are visible locally but not in Wazuh:

1. Confirm Sysmon is generating events locally.
2. Confirm the Wazuh Agent contains the Sysmon event-channel configuration.
3. Restart the Wazuh Agent.
4. Generate a new benign process event.
5. Verify the new Sysmon Event ID 1 locally.
6. Search for the new event in Wazuh.

Always generate a new event after changing or restarting telemetry components.
