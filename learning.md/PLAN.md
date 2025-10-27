learning/PLAN.md

This is my one-page learning plan for the month. I will complete and commit this file during the 15-minute selection clinic. It records the technology I chose to learn, why I chose it for my capstone, the three focused tasks I will complete, and the proof I will capture to show I did the work.

Student commitment

Name: Jordan Fields

Date created: 2025-10-27

I commit to treat this plan as my personal roadmap: I will keep dates realistic, finish each small task, capture evidence of success, and update this file if anything changes.

Chosen technology

Technology name: AI Log-Triage Assistant (OpenAI API or local LLM)

Technology version (if applicable): GPT-4/LLama 3 local build (tbd)

Why I chose this technology

This assistant will read Wazuh alert JSON, summarize what happened, map it to MITRE ATT&CK, and suggest response steps.
It enhances my Law Enforcement SOC project by automating Tier-1 alert triage and producing plain-language summaries for handoff—showing how modern SOCs use AI to speed incident response.

My three integration tasks (small, testable, dated)

Task 1 — Collect and summarize alerts

Description: Write a short Python script to read recent Wazuh alerts (JSON) and send them to an LLM prompt for summary and severity rating.

Start date: 2025-10-28

Target completion date: 2025-10-31

Success criterion: A sample alert produces a concise JSON summary (title, severity, MITRE ID, 3 recommended actions).

Proof method: Screenshot of terminal output and saved triage_output.json file in learning/README.md.

Where I will start Task 1: local branch feature/ai-triage-collector

Task 2 — Store and display AI triage results

Description: Extend the script to log each AI summary to a local file and show results in the VS Code terminal or Markdown table for demo purposes.

Start date: 2025-11-01

Target completion date: 2025-11-05

Success criterion: Multiple alerts produce separate summaries viewable in a Markdown table with timestamps.

Proof method: Screenshot of table view and copy of triage.log attached to learning/README.md.

Task 3 — Integrate triage summary into SOC workflow

Description: Simulate SOC analyst handoff by appending AI summaries to the Incident Response Plan template or Monday.com ticket note.

Start date: 2025-11-06

Target completion date: 2025-11-10

Success criterion: A completed incident record shows AI-generated summary + analyst verification note.

Proof method: Screenshot of final IRP section and Markdown snippet in learning/README.md.

Risks, assumptions, and blockers

Requires OpenAI API key or local LLM install.

Must redact sensitive alert data before sending to API.

Depends on Python requests and json libraries functioning locally.

My weekly timeline

Week 1: Commit PLAN and finish Task 1 (alert collection + AI summary).

Week 2: Complete Task 2 (storage + display demo).

Week 3: Integrate AI output into IR workflow (Task 3).

Week 4: Capture proof and draft learning/README.md + learning/REFLECTION.md.