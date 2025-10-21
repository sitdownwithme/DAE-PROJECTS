import random
from textwrap import dedent
# (optional) from itertools import cycle  # only needed if you later allow rounds > number of scenarios

SCENARIOS = [
    {
        "title": "Police HQ – Brute Force",
        "prompt": "200 failed logins on patrol DB in 10 minutes.",
        "choices": {
            "A": "Check SIEM auth dashboard + source IPs",
            "B": "Reboot database server immediately",
            "C": "Email whole department to change passwords"
        },
        "answer": "A",
        "why": "Verify in SIEM first (failed logins, geos, sources). Avoid knee-jerk reboot."
    },
    {
        "title": "911 CAD – Service Flap",
        "prompt": "`cad.service` restarts twice during peak calls.",
        "choices": {
            "A": "Place CAD in maintenance for an hour",
            "B": "Pull Filebeat logs (/var/log/syslog, auth) + check uptime monitors",
            "C": "Wipe and reinstall CAD"
        },
        "answer": "B",
        "why": "Confirm scope/impact via logs/monitoring; preserve availability first."
    },
    {
        "title": "Traffic Sensors – IoT Scan",
        "prompt": "Repeated TCP/23 probes on light controllers.",
        "choices": {
            "A": "Geo-block entire internet",
            "B": "Pivot in SIEM: source IP, rate limit, add Suricata rule",
            "C": "Ignore since it's only port 23"
        },
        "answer": "B",
        "why": "Investigate & mitigate precisely; add detection, not blanket blocks."
    },
    {
        "title": "Infra – Ransom Note",
        "prompt": "File `READ_ME.txt` appears on fileserver share.",
        "choices": {
                "A": "Isolate host from network; snapshot & hash evidence; notify IR",
                "B": "Open the note to see payment amount",
                "C": "Delete the note and hope it stops"
        },
        "answer": "A",
        "why": "Containment + evidence preservation + escalation is correct."
    },
    {
        "title": "Police HQ – Priv Esc",
        "prompt": "Helpdesk account briefly gained Domain Admin.",
        "choices": {
            "A": "Disable account; pull AD audit logs; start chain-of-custody",
            "B": "Reset domain functional level",
            "C": "Email admins to be careful"
        },
        "answer": "A",
        "why": "Contain suspected compromise & preserve audit trail."
    },
    {
        "title": "911 CAD – SSH Failures",
        "prompt": "50 failed SSH attempts from one IP in 3 minutes.",
        "choices": {
            "A": "Block the IP, verify in SIEM, review /var/log/auth.log via Filebeat",
            "B": "Turn off SSH everywhere",
            "C": "Change the CAD hostname"
        },
        "answer": "A",
        "why": "Targeted block + log verification; maintain service."
    },
]

def play(rounds=3):
    print("\n=== SOC INCIDENT GAME ===")
    score = 0

    # Pick unique scenarios for this session (no repeats)
    # Your menu only offers 3 or 5 rounds and you have 6 scenarios, so this is safe.
    scenarios = random.sample(SCENARIOS, k=min(rounds, len(SCENARIOS)))

    for i, s in enumerate(scenarios, start=1):
        print(f"\nRound {i}: {s['title']}")
        print(s["prompt"])
        for k, v in s["choices"].items():
            print(f"  {k}) {v}")
        pick = input("Your move (A/B/C): ").strip().upper()

        if pick == s["answer"]:
            print("✅ Correct!")
            score += 2
        else:
            print(f"❌ Not ideal. Best was {s['answer']}.")
        print("Why:", s["why"])

    print(f"\nFinal score: {score}/{rounds*2}")
    if score >= rounds*2-2:
        print("🛡️ Tier-1 SOC ready")
    else:
        print("🧭 Keep sharpening your playbooks")

if __name__ == "__main__":
    print(dedent("""
    Pick a quick mode:
      1) 3 rounds (demo)
      2) 5 rounds (full)
    """))
    m = input("Choose 1/2: ").strip()
    play(3 if m != "2" else 5)
