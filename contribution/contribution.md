CONTRIBUTION.md (Context Overview)
Purpose of My Contributions

This contribution series adds a unified, law-enforcement-focused SOC workflow to three separate open-source security repositories. The goal is to provide practical resources for SOC analysts working with macOS endpoints, ELK/Wazuh detections, digital investigations, and threat intelligence enrichment.

Each contribution represents a different phase of a real SOC workflow:

Detection (ELK/Wazuh + macOS logs)

Investigation (SOC analyst workflow)

Threat Intelligence (IOC enrichment)

Together, these three contributions form a complete end-to-end SOC process.

Repositories I Am Contributing To
1. DXC-0/SOC-Ressources

Link: https://github.com/DXC-0/SOC-Ressources

Contribution Focus:

Add macOS endpoint logging examples

Add ELK KQL detection queries

Provide Wazuh/ELK macOS integration configs

Create a new folder: macOS-Endpoint-Detection/
This covers the detection phase of the SOC workflow.

2. LetsDefend/awesome-soc-analyst

Link: https://github.com/LetsDefend/awesome-soc-analyst

Contribution Focus:

Add a “Law Enforcement SOC Investigation Workflow” section

Add macOS investigation cheat-sheets

Provide chain-of-custody steps for evidence handling
This covers the investigation & analyst workflow phase.

3. hslatman/awesome-threat-intelligence

Link: https://github.com/hslatman/awesome-threat-intelligence

Contribution Focus:

Add TI feeds relevant to macOS malware

Add regional/law-enforcement cyber-intel sources

Document how to enrich ELK/Wazuh alerts with TI
This covers the threat-intelligence enrichment phase.

Why These Contributions Matter

They provide missing macOS endpoint coverage in SOC resources

They map detection → investigation → TI in one unified narrative

They create a structured example useful for SOC analysts, students, and blue-team beginners

They introduce law-enforcement-style evidence handling into existing repos

They show how Wazuh + ELK + TI can be integrated for real-world SOC workflows

Summary of My Contribution Series

I am contributing a complete, law-enforcement-oriented SOC workflow across three separate security repositories.

Repo 1: Detection (macOS logs + ELK/Wazuh queries)
Repo 2: Investigation (analyst workflow, chain of custody)
Repo 3: Threat Intelligence (IOC feeds & enrichment)

Together, these contributions form a full end-to-end SOC process that I developed as part of my cybersecurity project.

Status

Phase 1 (Detection Repo) → In progress

Phase 2 (Investigation Repo) → Drafting

Phase 3 (Threat Intel Repo) → Drafting

If you want, I can also generate:

✔️ A README section describing your contribution
✔️ The exact folders + filenames for each repo
✔️ Fully written markdown files ready to upload
✔️ Your PR descriptions for all three repos

Just say the word: “Draft the files.”# 📘 Observability & Logging: Project Notes
This document tracks the observability work completed as part of the **AI Log-Triage Assistant** integration for the Law Enforcement SOC project.  
Notes reflect progress from the learning plan created on 2025-10-27.

---

## 1. Health Check Endpoint

Have you implemented a health-check endpoint?

- [x] Yes  
- [ ] No  
- [ ] Not applicable to my project

**Your endpoint path:**  
`/health`

### Sample output:
```json
{
  "status": "ok",
  "uptime": "running",
  "version": "ai-triage-v1"
}
Why is this useful?
I added a health-check endpoint so I can verify that the triage collector script and AI inference service (OpenAI API or local LLaMA3) are reachable.
This supports SOC workflows where automated jobs need to confirm the model is up before sending alerts for summary.

2. Health Check Test
Did you write a test for the health-check endpoint?

 Yes

 No

Test code or description:
python
Copy code
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
This test ensures that before running the AI triage cycle, the system is alive and ready to process Wazuh alert JSON.

3. Log Event or Metric
Name of log event or metric:
ai_alert_triage_summary_generated

What triggers this?
This logs every time the triage script reads a Wazuh alert JSON and generates an AI summary (Task 1 and Task 2 from the PLAN).
Events occur each time a new alert is collected and appended to triage.log.

Sample output format or log:
json
Copy code
{
  "event": "ai_alert_triage_summary_generated",
  "alert_id": "wazuh_00438",
  "severity_ai": 4,
  "mitre_id": "T1059",
  "timestamp": "2025-10-31T16:22:10Z"
}
Where is this implemented?
triage.py → save_log(summary) function
(Task 2 – “Store and display AI triage results”)

4. Optional Monitoring Tools
Did you use monitoring tools (Grafana, Prometheus, Kibana, etc.)?

 Yes

 No

Tool name(s):
Wazuh Dashboard (alert stream monitoring)

Potential Kibana visualization

Local LLM metrics (Ollama dashboard, if used)

Screenshot or description:
The Wazuh dashboard shows new alerts being generated, which feed into the AI triage script.
Triage logs are stored locally and can be converted to Markdown tables for demo purposes.

Example display includes:

alert count

rule level

source IPs

timestamp

severity indicators

This supports Task 2 & Task 3 in monitoring AI triage output.

5. Reflection & Learning
What did you learn while implementing observability?
I learned that storing structured outputs from the AI model makes SOC handoff smoother and easier to follow. Logging each summary with timestamps creates an audit trail—critical in a real SOC or law enforcement environment. I also learned how to collect alerts from Wazuh in JSON format and route them through an LLM for classification and recommendations.

Anything you would do differently or improve?
I would add more internal logs—like when the script fails to reach the model or when an alert is malformed. I would also add metrics for triage response time and success rate, and integrate a dashboard (Grafana) to show AI-triage activity over time.

