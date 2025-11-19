# 📘 Mini-Tutorial: AI Log-Triage Assistant for Wazuh Alerts

_A student-authored tutorial documenting a key integration learned in Semester 5._

---

## ❓ What This Teaches

This tutorial teaches how to build an **AI-powered log triage assistant** that reads Wazuh alert JSON, summarizes the event, maps it to MITRE ATT&CK, and provides recommended response steps. The goal is to automate Tier-1 SOC triage, reduce alert fatigue, and produce clear summaries that law enforcement or SOC teams can quickly understand. This integration is ideal for **SOC analyst workflows, IR pipelines, home labs, Wazuh-based SIEM projects, and cybersecurity demonstrations**, especially when showcasing modern AI-assisted SOC capabilities.

---

## 🎯 Use Case

> What real-world need or job scenario does this apply to?

-   [ ] Backend development  
-   [x] Cybersecurity  
-   [x] Monitoring / Observability  
-   [x] Performance / Testing  
-   [ ] Authentication / Authorization  
-   [x] DevOps / Deployments  
-   [x] Other: _Security Operations (SOC), Incident Response (IR), Law Enforcement Cyber Units_

---

## 🚀 Quick Setup / Install

You only need Python + a model (OpenAI API or local LLaMA/Mistral via Ollama).

```bash
pip install requests python-dotenv
