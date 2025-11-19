# 📘 Observability & Logging: Project Notes
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

