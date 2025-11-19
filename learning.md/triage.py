import json
import requests
from datetime import datetime

def read_alert(path="alert.json"):
    with open(path, "r") as f:
        return json.load(f)

def send_to_ai(alert_data):
    prompt = f"""
    You are an AI SOC assistant. Summarize this Wazuh alert with:
    - title
    - severity (1–5)
    - MITRE ATT&CK technique ID (best guess)
    - 3 recommended response steps
    
    Alert:
    {json.dumps(alert_data)}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt}
    )
    return response.json()

alert = read_alert()
summary = send_to_ai(alert)

with open("triage_output.json", "w") as f:
    json.dump(summary, f, indent=4)

print("Summary saved to triage_output.json")
