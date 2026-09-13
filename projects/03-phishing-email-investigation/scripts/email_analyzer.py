import json
import re
import subprocess
import urllib.request

MAILPIT_API = "http://127.0.0.1:8025/api/v1/messages"
MAILPIT_BASE = "http://127.0.0.1:8025"

def get_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

def get_text(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8", errors="replace")
def write_windows_event(event_data):
    event_message = json.dumps(event_data, separators=(",", ":"))

    # Escape single quotes for PowerShell
    safe_message = event_message.replace("'", "''")

    command = (
        "Write-EventLog "
        "-LogName Application "
        "-Source 'SOC-EmailSecurity' "
        "-EventId 3101 "
        "-EntryType Warning "
        f"-Message '{safe_message}'"
    )

    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("Windows Event : CREATED - Event ID 3101")
    else:
        print("Windows Event : FAILED")
        print(result.stderr)

# Get message list
data = get_json(MAILPIT_API)

if not data.get("messages"):
    print("No messages found.")
    raise SystemExit

# Newest message
message = data["messages"][0]

message_id = message["ID"]
sender = message["From"]["Address"]
subject = message.get("Subject", "")
reply_to = ""

if message.get("ReplyTo"):
    reply_to = message["ReplyTo"][0].get("Address", "")

attachments = message.get("Attachments", 0)

body_url = f"{MAILPIT_BASE}/view/{message_id}.txt"
body = get_text(body_url)

combined = f"{subject} {body}".lower()

score = 0
reasons = []

urgency_terms = [
    "urgent",
    "immediately",
    "expires today",
    "expire today",
    "account suspended",
    "mailbox suspended"
]

credential_terms = [
    "verify your account",
    "verify account",
    "password",
    "login",
    "sign in"
]

for term in urgency_terms:
    if term in combined:
        score += 1
        reasons.append(f"urgency:{term}")

for term in credential_terms:
    if term in combined:
        score += 1
        reasons.append(f"credential_request:{term}")

urls = re.findall(r'https?://[^\s<>"\']+', body)

if urls:
    score += 1
    reasons.append(f"url_present:{len(urls)}")

if reply_to:
    sender_domain = sender.split("@")[-1].lower()
    reply_domain = reply_to.split("@")[-1].lower()

    if sender_domain != reply_domain:
        score += 2
        reasons.append("reply_to_domain_mismatch")

if attachments > 0:
    score += 1
    reasons.append(f"attachments:{attachments}")

if score >= 4:
    verdict = "suspicious"
    severity = "high"
elif score >= 2:
    verdict = "suspicious"
    severity = "medium"
else:
    verdict = "benign"
    severity = "informational"

print("=" * 60)
print("SOC EMAIL ANALYZER")
print("=" * 60)
print(f"Sender      : {sender}")
print(f"Reply-To    : {reply_to if reply_to else 'None'}")
print(f"Subject     : {subject}")
print(f"Attachments : {attachments}")
print(f"URLs        : {urls if urls else 'None'}")
print(f"Score       : {score}")
print(f"Verdict     : {verdict}")
print(f"Severity    : {severity}")
print("Reasons     :")

if reasons:
    for reason in reasons:
        print(f"  - {reason}")
if verdict == "suspicious":
    event_data = {
        "event_type": "phishing_detection",
        "message_id": message_id,
        "sender": sender,
        "reply_to": reply_to if reply_to else "",
        "subject": subject,
        "attachments": attachments,
        "urls": urls,
        "score": score,
        "verdict": verdict,
        "severity": severity,
        "reasons": reasons
    }

    write_windows_event(event_data)
else:
    print("  - No suspicious indicators detected")