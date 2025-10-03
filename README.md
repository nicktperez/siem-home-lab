SIEM Home Lab

Overview

This repository contains a home lab environment for building a Security Information and Event Management (SIEM) platform using the Elastic Stack (Elasticsearch, Logstash, Kibana) with Filebeat.

The project demonstrates log collection, parsing, detection engineering, and dashboard creation for security monitoring. It grows in phases to simulate how an enterprise SIEM might evolve, including advanced work with AI-related threats.

⸻

Current Features
	•	Docker-based Elastic Stack (Elasticsearch, Logstash, Kibana)
	•	Filebeat integration for log shipping
	•	Custom Logstash pipeline for parsing syslog and SSH events
	•	Python log generator to simulate brute-force attempts
	•	Logstash aggregation that detects repeated failed logins
	•	Exported Kibana dashboards to visualize alerts

⸻

Repository Structure
	•	docker-compose.yml – starts Elasticsearch, Logstash, and Kibana containers
	•	configs/logstash/pipeline/logstash.conf – defines the Logstash pipeline for parsing logs
	•	configs/filebeat/filebeat.yml – example Filebeat configuration
	•	scripts/generate_syslog.py – generates simulated SSH brute-force logs
	•	dashboards/ssh_bruteforce_dashboard.ndjson – exported Kibana dashboard
	•	README.md – project documentation

⸻

Setup Instructions
	1.	Clone the repository and navigate into the project directory
	2.	Start the Elastic Stack:
docker compose up -d
	3.	Install Filebeat (example for macOS using Homebrew):
brew install filebeat
	4.	Update the Filebeat configuration at /opt/homebrew/etc/filebeat/filebeat.yml
	5.	Start Filebeat:
brew services start filebeat
	6.	Generate test logs:
python3 scripts/generate_syslog.py
	7.	Access Kibana at http://localhost:5601

⸻

Dashboards and Alerts

The repository includes a Kibana dashboard to visualize SSH brute-force alerts.

Visualizations include:
	•	Top Attacker IPs: shows the IPs responsible for failed SSH login attempts
	•	Alerts Over Time: shows alert frequency across a selected time range

Import instructions:
	1.	In Kibana, navigate to Stack Management > Saved Objects > Import
	2.	Select the file dashboards/ssh_bruteforce_dashboard.ndjson
	3.	If prompted with a Data View Conflict, associate with the data view for alerts-ssh-* and ensure the timestamp field is @timestamp

⸻

Roadmap

The project is being developed in phases to simulate the growth of a SIEM in an enterprise setting.

Phase 1 – Foundation (Completed)

This phase established the core SIEM environment using the Elastic Stack (Elasticsearch, Logstash, Kibana) and Filebeat. It provided the initial end-to-end pipeline for collecting logs, parsing them, generating detections, and visualizing results.

Completed work:
	•	Deployed a Docker-based Elastic Stack consisting of Elasticsearch, Logstash, and Kibana.
	•	Created docker-compose.yml for reproducible stack deployment.
	•	Configured Filebeat on macOS to ship local system logs (/var/log/*.log, /private/var/log/*.log) into Logstash.
	•	Built a custom Logstash pipeline (configs/logstash/pipeline/logstash.conf) that parses syslog messages and extracts relevant fields such as message, host, and src_ip.
	•	Developed a Python script scripts/generate_syslog.py to simulate SSH brute-force attacks by sending multiple failed login events.
	•	Implemented Logstash aggregation logic to detect repeated failed SSH login attempts from the same source IP within a short time window.
	•	Configured outputs so that detections are indexed into a dedicated alerts index (alerts-ssh-*) while raw logs flow into syslog-*.
	•	Verified pipeline functionality by generating synthetic logs and confirming successful indexing in Elasticsearch.
	•	Built and exported a Kibana dashboard with two visualizations:
	•	Top Attacker IPs – bar chart showing IPs with the highest number of failed SSH attempts.
	•	Alerts Over Time – time-series chart of brute-force alerts, showing spikes during simulated attacks.

Detection logic:
	•	Threshold-based detection: if a single IP generates ≥5 failed SSH logins in under 1 minute, an alert document is written to alerts-ssh-*.
	•	Alerts include fields such as src_ip, message, and timestamp for investigation.
	•	Analysts can correlate alert data with raw syslog entries (syslog-*) to review the attack pattern.

Next steps from this foundation:
	•	Extend ingestion to additional log sources (Windows, web server, firewall).
	•	Develop more advanced detection rules beyond brute-force thresholds.
	•	Build a “Global Security Overview” dashboard combining multiple sources.

Phase 2 – Add More Log Sources (In Progress)
	•	Windows logs via Winlogbeat or Sysmon
	•	Web server logs with Filebeat
	•	Simulated firewall logs

Phase 3 – Expand Detection Rules (Planned)
	•	Windows failed login thresholds
	•	Windows persistence (new user created)
	•	Web reconnaissance (multiple 404s)
	•	Firewall port scans

Phase 4 – Additional Dashboards (Planned)
	•	Windows dashboard
	•	Web dashboard
	•	Firewall dashboard
	•	Combined security overview

Phase 5 – Case Study Documentation (Planned)
	•	Walkthroughs of simulated incidents
	•	Example SOC response workflows

Phase 6 – Threat Intelligence Enrichment (Planned)
	•	Integration with AlienVault OTX or AbuseIPDB
	•	Tag alerts with known malicious indicators

Phase 7 – AI and Emerging Threats: Prompt Injection (Completed)

This phase introduces AI-specific log ingestion and detection to keep the lab aligned with emerging security challenges. The initial focus is on prompt injection detection — a growing risk in LLM-powered applications.

Completed work:
	•	Added scripts/generate_prompt_injection.py, a Python generator that produces synthetic AI prompt logs (normal + injection attempts).
	•	Created a dedicated Logstash pipeline (configs/logstash/pipeline/ai_prompt.conf) to ingest JSON prompt logs and apply regex-based detection.
	•	Configured pipeline to index all prompts into ai-prompts-* and suspicious prompts into alerts-ai-*.
	•	Updated docker-compose.yml to expose Logstash on TCP port 5000 for AI prompt ingestion.
	•	Verified detections by generating simulated events and viewing them in Kibana.

Detection logic:
	•	Regex-based detection flags prompt text containing phrases like:
	•	“ignore your previous instructions”
	•	“output the admin password”
	•	“print the API key”
	•	“exfiltrate”
	•	Alerts are tagged with ai_prompt_injection and written to alerts-ai-*.

Next steps in AI & Emerging Threats:
	•	Expand detection beyond regex with token-length anomalies and semantic similarity.
	•	Add telemetry for LLM API misuse (e.g., excessive tokens, unusual rate of calls).
	•	Simulate AI-generated phishing attempts.
	•	Enrich detections with external threat intelligence.

⸻

Learning Outcomes
	•	Building and managing a SIEM pipeline
	•	Configuring log collection with Filebeat
	•	Writing parsing and aggregation rules in Logstash
	•	Generating synthetic attack data for testing
	•	Creating dashboards and alerts in Kibana
	•	Documenting the growth of a SIEM through iterative phases
	•	Considering AI-related threats and modern detection strategies

⸻

Notes
	•	This lab is intended for educational and demonstration purposes
	•	The pipeline can be extended to other log sources and detection use cases
	•	Dashboards and exports are included for reproducibility
