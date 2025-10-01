---
title: "Projects"
permalink: /projects/
---

<div class="project-item" id="Incident Response PlayBook">
  <h2>Incident Response PlayBook</h2>
  
  <div style="display: flex; flex-wrap: wrap; gap: 2rem; margin-bottom: 2rem;">
    <div style="flex: 0 0 300px;">
      <img src="/assets/img/incident_response_playbook.png" alt="Incident Response Playbook Screenshot" style="width: 100%; border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    </div>
    
    <div style="flex: 1; min-width: 300px;">
      <h3>Overview</h3>
      <p>
        The Incident Response Playbook is a cybersecurity project designed to simulate ransomware attacks and practice full-cycle response. Built in an isolated lab with <strong>pfSense, ELK Stack, Wazuh, Sysmon, and Metasploit</strong>, the project applied the <strong>NIST 800-61 framework</strong> for detection, containment, eradication, and recovery. It included forensic evidence collection and detailed documentation to strengthen both attacker and defender perspectives.
      </p>
      
      <h3>Technologies Used</h3>
      <ul>
        <li>pfSense firewall</li>
        <li>Windows Server</li>
        <li>Linux (Apache, Postfix)</li>
        <li>ELK Stack</li>
        <li>Wazuh</li>
        <li>Sysmon</li>
        <li>Metasploit</li>
        <li>DVWA</li>
        <li>Kali Linux</li>
      </ul>
      
      <h3>Key Learnings</h3>
      <p>
        Learned how to integrate SIEM tools, analyze alerts, and document incidents in line with cybersecurity frameworks. Gained practical skills in log analysis, forensic data collection, and developing playbooks that can be applied in both corporate and law enforcement SOC workflows.
      </p>
      
      <div>
        <a href="https://github.com/sitdownwithme/incident-response-playbook" target="_blank" class="btn btn--primary">View Code</a>
        <a href="#" target="_blank" class="btn btn--secondary">Documentation</a>
      </div>
    </div>
  </div>
</div>

<hr>

<div class="project-item" id="Sports Connect">
  <h2>Sports Connect</h2>
  
  <div style="display: flex; flex-wrap: wrap; gap: 2rem; margin-bottom: 2rem;">
    <div style="flex: 0 0 300px;">
      <img src="/assets/img/project3-placeholder.jpg.svg" alt="Sports Connect Screenshot" style="width: 100%; border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    </div>
    
    <div style="flex: 1; min-width: 300px;">
      <h3>Overview</h3>
      <p>
        Sports Connect is a web application created to connect athletes, coaches, and teams. While primarily a development project, it emphasized <strong>secure user authentication and database access controls</strong> — introducing me to access management, data security, and the importance of protecting sensitive user information, which directly translates into SOC analyst responsibilities.
      </p>
      
      <h3>Technologies Used</h3>
      <ul>
        <li>HTML/CSS</li>
        <li>JavaScript</li>
        <li>Responsive design</li>
        <li>User authentication</li>
        <li>Database management</li>
      </ul>
      
      <h3>Key Learnings</h3>
      <p>
        Gained foundational knowledge in securing web applications, including login workflows and database protection. Learned how access control ties into monitoring and how security-by-design complements SOC detection and response practices.
      </p>
      
      <div>
        <a href="https://github.com/sitdownwithme/sports-connect" target="_blank" class="btn btn--primary">View Code</a>
        <a href="#" target="_blank" class="btn btn--secondary">Documentation</a>
      </div>
    </div>
  </div>
</div>

<hr>

<div class="project-item" id="Mini SOC Project">
  <h2>Mini SOC Project</h2>
  
  <div style="display: flex; flex-wrap: wrap; gap: 2rem; margin-bottom: 2rem;">
    <div style="flex: 0 0 300px;">
      <img src="/assets/img/mini_soc.png" alt="Mini SOC Project Screenshot" style="width: 100%; border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    </div>
    
    <div style="flex: 1; min-width: 300px;">
      <h3>Overview</h3>
      <p>
        The Mini SOC Project is a training lab built to simulate real Security Operations Center workflows. It covers <strong>log collection, SIEM dashboards, detection engineering, and case reporting</strong>. Attack simulations such as brute force and phishing validate detection rules, while case management tools document incidents as if handling real investigations.
      </p>
      
      <h3>Technologies Used</h3>
      <ul>
        <li>VirtualBox (Ubuntu, Windows, Parrot)</li>
        <li>ELK Stack or Splunk</li>
        <li>Wazuh</li>
        <li>Suricata</li>
        <li>Filebeat / Winlogbeat</li>
        <li>Python, Bash scripting</li>
      </ul>
      
      <h3>Key Learnings</h3>
      <p>
        Strengthened foundational SOC skills by building dashboards, writing detection rules, and creating incident response playbooks. Learned how to document investigations with evidence screenshots and workflows, laying the groundwork for advanced law enforcement SOC analysis.
      </p>
      
      <div>
        <a href="https://github.com/sitdownwithme/mini-soc-project" target="_blank" class="btn btn--primary">View Code</a>
        <a href="#" target="_blank" class="btn btn--secondary">Documentation</a>
      </div>
    </div>
  </div>
</div>

<hr>

<div class="project-item" id="Law Enforcement SOC Project">
  <h2>Law Enforcement SOC Project</h2>
  
  <div style="display: flex; flex-wrap: wrap; gap: 2rem; margin-bottom: 2rem;">
    <div style="flex: 0 0 300px;">
      <img src="/assets/img/law_enforcement_soc.png" alt="Law Enforcement SOC Project Screenshot" style="width: 100%; border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    </div>
    
    <div style="flex: 1; min-width: 300px;">
      <h3>Overview</h3>
      <p>
        This capstone project expands the Mini SOC into a <strong>law enforcement-focused SOC lab</strong> that simulates protecting municipal infrastructure like 911 CAD systems, evidence databases, and surveillance networks. It integrates <strong>custom SIEM detection rules, law enforcement playbooks, and court-admissible chain-of-custody documentation</strong>.
      </p>
      
      <h3>Technologies Used</h3>
      <ul>
        <li>ELK Stack or Splunk</li>
        <li>Wazuh (File Integrity Monitoring)</li>
        <li>Suricata (Network IDS)</li>
        <li>Syslog-ng / Rsyslog</li>
        <li>Python automation scripts</li>
        <li>MD5/SHA256 hash verification</li>
      </ul>
      
      <h3>Key Learnings</h3>
      <p>
        Gained experience in high-stakes SOC workflows where cybersecurity meets criminal justice. Learned how to produce legally defensible documentation, build specialized detection rules for law enforcement systems, and coordinate incident response in a multi-agency environment.
      </p>
      
      <div>
        <a href="https://github.com/sitdownwithme/law-enforcement-soc" target="_blank" class="btn btn--primary">View Code</a>
        <a href="#" target="_blank" class="btn btn--secondary">Documentation</a>
      </div>
    </div>
  </div>
</div>

<div style="text-align: center; margin-top: 3rem;">
  <img src="/assets/img/dae.png" alt="dae logo" style="max-width: 150px; height: auto;">
</div>
