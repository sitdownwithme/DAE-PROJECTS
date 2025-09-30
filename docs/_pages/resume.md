---
layout: page
title: "Resume"
permalink: /resume/
---

<div style="text-align: center; margin-bottom: 2rem;">
  <a href="{{ '/assets/files/jordan-fields-resume.pdf' | relative_url }}" target="_blank" class="btn btn--primary"><i class="fas fa-download"></i> Download PDF Resume</a>
</div>

# Cybersecurity SOC Analyst Resume

## Education
**DAE Institute**  
*Expected Graduation: December 2025*

Studying cybersecurity with a focus on security operations, incident response, and threat detection.

**Relevant Coursework:** Python Programming, Cybersecurity Fundamentals, Digital Forensics, Network Security

---

## Technical Skills

### Security Operations & Monitoring
- SIEM Platforms (ELK Stack, Splunk)
- Log Analysis & Correlation
- Threat Detection & Response
- File Integrity Monitoring (Wazuh)
- Network Traffic Analysis

### Digital Forensics & Investigation
- Chain-of-Custody Documentation
- Evidence Preservation & Hash Verification
- Incident Timeline Reconstruction
- Security Alert Investigation
- Forensics Tools (Sysmon, Autopsy basics)

### Programming & Automation
- Python (Security automation, log parsing, IOC extraction)
- PowerShell (Windows security monitoring)
- Bash scripting (Linux log analysis)

### Security Tools & Technologies
- **SIEM:** ELK Stack, Wazuh, Splunk
- **Network Security:** pfSense, Suricata, Wireshark, Zeek
- **Attack Simulation:** Kali Linux, Nmap, Metasploit, Hydra
- **Forensics:** Sysmon, FTK Imager, hash utilities (MD5/SHA256)
- **Platforms:** Git/GitHub, VS Code, Windows Server, Linux

---

## Cybersecurity Projects

### Law Enforcement SOC Lab: Municipal Infrastructure Protection
*September 2025 - December 2025 (In Progress)*

**Project Overview:** Building a comprehensive Security Operations Center environment simulating protection of municipal law enforcement systems, focusing on critical infrastructure monitoring and digital evidence chain-of-custody management.

**Core Infrastructure:**
- Deployed 4-VM simulated municipal network (911 CAD System, Evidence Management Database, Surveillance Network Controller, Officer Workstation)
- Configured ELK Stack SIEM with legal compliance logging and evidence audit trails
- Implemented file integrity monitoring with Wazuh for evidence tampering detection

**Detection & Monitoring:**
- Developing 8–10 custom SIEM detection rules for law-enforcement scenarios (unauthorized database queries, evidence tampering, credential compromise, data exfiltration)
- Creating 5–7 specialized dashboards for critical system monitoring and chain-of-custody audit trails
- Building automated alerting for insider threats and privilege escalation attempts

**Incident Response & Documentation:**
- Designing 6–8 LE-specific incident response playbooks (ransomware on 911 systems, compromised credentials, surveillance breaches, insider threats)
- Executing 8 attack simulations including brute force, phishing, ransomware, and data exfiltration scenarios
- Documenting 10–12 investigations with court-admissible chain-of-custody procedures and evidence hash verification

**Automation & Compliance:**
- Developing Python scripts for automated chain-of-custody report generation with timestamps and digital fingerprints
- Implementing real-time file integrity monitoring with automated alerting to SIEM
- Creating legal admissibility checklists and evidence handling procedures

**Key Technologies:** ELK Stack, Wazuh, Suricata, Python, PowerShell, Kali Linux, PostgreSQL, Windows Server, Syslog-ng, Metasploit, Nmap, Hydra

**Portfolio Deliverables:** GitHub repository with SIEM configurations and detection rules, 10–12 documented case investigations, incident response playbook library, demo video showcasing live attack detection and response

---

### Incident Response Playbook & Lab Environment
*June 2025*

**Project & Role:** Designed and implemented an Incident Response Lab to simulate a ransomware attack on high-value confidential data, serving as both lab architect and incident response playbook developer.

**Security Operations:**
- Built isolated network environment with pfSense firewall, Windows Server, and Linux systems
- Deployed ELK Stack SIEM with Wazuh for real-time threat detection and log correlation
- Configured Sysmon for advanced Windows endpoint monitoring and forensic data collection

**Incident Response Development:**
