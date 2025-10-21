# Law Enforcement SOC Project — Daily Timeline
*(Tuesday Oct 7 – Thursday Nov 20 2025 | Monday–Thursday Only)*  

---

## Day 1 — Oct 7 (Tue)
**Main Task:** Reset project timeline & GitHub repo  
**Sub-Item (Rule Brick):** Apply Vulnerability Assessment Techniques  
**Sub-Item Comment:** Plan initial asset discovery using Nmap/OpenVAS; outline scan objectives.

---

## Day 2 — Oct 8 (Wed)
**Main Task:** Review Final SOC Design + IDP goals  
**Sub-Item (Rule Brick):** Apply Vulnerability Assessment Techniques  
**Sub-Item Comment:** Document asset identification strategy; list critical systems (Police HQ, 911, Traffic).

---

## Day 3 — Oct 9 (Thu)
**Main Task:** Build base lab environment in VirtualBox  
**Sub-Item (Rule Brick):** Apply Vulnerability Assessment Techniques  
**Sub-Item Comment:** Configure Nmap scan of internal lab; begin network mapping documentation.

---

## Day 4 — Oct 13 (Mon)
**Main Task:** Install Wazuh SIEM on Ubuntu  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Verify event ingestion and baseline alerting within SIEM.

---

## Day 5 — Oct 14 (Tue)
**Main Task:** Connect Filebeat + Winlogbeat agents → Wazuh  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Test real-time alerts; validate data flow from endpoints.

---

## Day 6 — Oct 15 (Wed)
**Main Task:** Configure pfSense Syslog → SIEM  
**Sub-Item (Rule Brick):** Apply Vulnerability Assessment Techniques  
**Sub-Item Comment:** Document exposed ports/services from pfSense; assess firewall rules.

---

## Day 7 — Oct 16 (Thu)
**Main Task:** Validate and tune log ingestion  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Tune alert thresholds and confirm healthy log pipeline.

---

## Day 8 — Oct 20 (Mon)
**Main Task:** Create detection rules (Brute Force, Phish, Malware)  
**Sub-Item (Rule Brick):** Identify & Analyze Cyber Threats  
**Sub-Item Comment:** Build rules mirroring APT behavior; document detection indicators.

---

## Day 9 — Oct 21 (Tue)
**Main Task:** Write Incident Response Playbook #1 (Phishing)  
**Sub-Item (Rule Brick):** Identify & Analyze Cyber Threats  
**Sub-Item Comment:** Use SET in Parrot OS to generate phishing template and capture indicators.

---

## Day 10 — Oct 22 (Wed)
**Main Task:** Write Playbook #2 (Malware Infection)  
**Sub-Item (Rule Brick):** Identify & Analyze Cyber Threats  
**Sub-Item Comment:** Upload malware sample to VirusTotal; document behavioral results.

---

## Day 11 — Oct 23 (Thu)
**Main Task:** Write Playbook #3 (Brute Force Attempt)  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Simulate brute-force attack; observe Wazuh detection workflow.

---

## Day 12 — Oct 27 (Mon)
**Main Task:** Build SOC Dashboards inside Wazuh  
**Sub-Item (Rule Brick):** Implement Threat Intelligence Principles  
**Sub-Item Comment:** Create 3 dashboards (Login Anomalies, Network Traffic, System Health) and map IoCs to MITRE ATT&CK.

---

## Day 13 — Oct 28 (Tue)
**Main Task:** Simulate 911 CAD logs via Filebeat (Linux)  
**Sub-Item (Rule Brick):** Implement Threat Intelligence Principles  
**Sub-Item Comment:** Analyze IoCs; confirm Filebeat log patterns visible in Wazuh dashboard.

---

## Day 14 — Oct 29 (Wed)
**Main Task:** Add Traffic Sensor (IoT) log source  
**Sub-Item (Rule Brick):** Apply Vulnerability Assessment Techniques  
**Sub-Item Comment:** Run asset scan on IoT devices; document discovered risks.

---

## Day 15 — Oct 30 (Thu)
**Main Task:** Correlate alerts across Police HQ ↔ 911 ↔ Traffic  
**Sub-Item (Rule Brick):** Implement Threat Intelligence Principles  
**Sub-Item Comment:** Demonstrate cross-system correlation using OpenCTI feeds.

---

## Day 16 — Nov 3 (Mon)
**Main Task:** Draft Chain-of-Custody + Evidence Form  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Identify critical risks from scan results; plan mitigation workflow.

---

## Day 17 — Nov 4 (Tue)
**Main Task:** Test evidence workflow on two sample cases  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Document mitigation actions and update risk tracker sheet.

---

## Day 18 — Nov 5 (Wed)
**Main Task:** Design Incident Case Report template (MD → PDF)  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Link risk findings to incident report workflow.

---

## Day 19 — Nov 6 (Thu)
**Main Task:** Complete 3 sample case reports (Phish, Malware, Brute Force)  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Classify incidents, prioritize alerts, and log response outcomes.

---

## Day 20 — Nov 10 (Mon)
**Main Task:** Expand Wazuh Dashboards for Critical Infrastructure  
**Sub-Item (Rule Brick):** Implement Threat Intelligence Principles  
**Sub-Item Comment:** Add panels for 911 (Filebeat), Traffic (Syslog), Infra (Suricata); finalize “SOC Command Center” dashboard.

---

## Day 21 — Nov 11 (Tue)
**Main Task:** Run SOC Simulation Test (End-to-End)  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Validate SOC playbook accuracy; verify alert triggers and evidence tracking.

---

## Day 22 — Nov 12 (Wed)
**Main Task:** Perform SIEM Optimization & Rule Tuning  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Document risk of alert fatigue and optimize alert thresholds.

---

## Day 23 — Nov 13 (Thu)
**Main Task:** Review SOC Workflow & Fix Detection Gaps  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Verify detection coverage; retest and confirm accuracy.

---

## Day 24 — Nov 17 (Mon)
**Main Task:** Compile Final SOC Documentation (Methods + Findings)  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Link documentation to risk findings and mitigation results.

---

## Day 25 — Nov 18 (Tue)
**Main Task:** Write Executive Summary & Lessons Learned  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Summarize risk posture improvements and lessons from simulation.

---

## Day 26 — Nov 19 (Wed)
**Main Task:** Verify All Deliverables (Logs, Playbooks, Reports)  
**Sub-Item (Rule Brick):** Implement Security Monitoring & Incident Response  
**Sub-Item Comment:** Ensure all artifacts validated for presentation.

---

## Day 27 — Nov 20 (Thu)
**Main Task:** Submit Final SOC Project & Reflection  
**Sub-Item (Rule Brick):** Develop & Apply Risk Management Strategies  
**Sub-Item Comment:** Evaluate overall SOC readiness and system performance.

---

## Day 28 — (Reserve Buffer)
**Main Task:** Optional review or demo prep if needed  
**Sub-Item (Rule Brick):** —  
**Sub-Item Comment:** —  

---

# ✅ Phase Summary
**Phase 1 (Setup):** Days 1-7  
**Phase 2 (Detection & Playbooks):** Days 8-11  
**Phase 3 (Intel & Correlation):** Days 12-15  
**Phase 4 (Evidence & Risk Mgmt):** Days 16-19  
**Phase 5 (Optimization & Delivery):** Days 20-27  
