SIEM Home Lab

This repository contains a home lab environment for building a Security Information and Event Management (SIEM) platform using the Elastic Stack (Elasticsearch, Logstash, Kibana) with Filebeat. The project demonstrates log collection, parsing, detection engineering, and dashboard creation for security monitoring.

⸻

Overview

The lab currently includes:
	•	A Docker-based Elastic Stack (Elasticsearch, Logstash, Kibana).
	•	Filebeat integration for log shipping.
	•	A custom Logstash pipeline for parsing syslog and SSH events.
	•	A Python log generator to simulate brute-force attempts.
	•	A Logstash-based aggregation that detects repeated failed logins.
	•	Exported Kibana dashboards to visualize alerts.

⸻

Repository Structure
	•	docker-compose.yml – starts Elasticsearch, Logstash, and Kibana containers.
	•	configs/logstash/pipeline/logstash.conf – defines the Logstash pipeline for parsing logs.
	•	configs/filebeat/filebeat.yml – example Filebeat configuration.
	•	scripts/generate_syslog.py – generates simulated SSH brute-force logs.
	•	dashboards/ssh_bruteforce_dashboard.ndjson – exported Kibana dashboard.
	•	README.md – project documentation.

⸻

Setup Instructions
	1.	Clone the repository and navigate into the project directory.
	2.	Start the Elastic Stack:
docker compose up -d
	3.	Install Filebeat (macOS example using Homebrew):
brew install filebeat
	4.	Update the Filebeat configuration at /opt/homebrew/etc/filebeat/filebeat.yml.
	5.	Start Filebeat:
brew services start filebeat
	6.	Generate test logs:
python3 scripts/generate_syslog.py
	7.	Access Kibana at:
http://localhost:5601

⸻

Dashboards and Alerts

The repository includes a Kibana dashboard to visualize SSH brute-force alerts.

Visualizations:
	•	Top Attacker IPs – shows the IPs responsible for failed SSH login attempts.
	•	Alerts Over Time – shows alert frequency across a selected time range.

Import Instructions:
	1.	In Kibana, navigate to Stack Management > Saved Objects > Import.
	2.	Select the file dashboards/ssh_bruteforce_dashboard.ndjson.
	3.	If prompted with a Data View Conflict, associate with the data view for alerts-ssh-* and ensure the timestamp field is @timestamp.

⸻

Roadmap

The project is being developed in phases to simulate the growth of a SIEM in an enterprise setting. Each phase will be documented and committed to this repository.

Phase 1 – Foundation (Completed)
	•	Deploy Elastic Stack with Docker.
	•	Configure Filebeat to ship macOS system logs.
	•	Write Logstash pipeline to parse SSH failed logins.
	•	Simulate SSH brute-force attacks with Python script.
	•	Detect repeated failed logins with Logstash aggregation.
	•	Output alerts to a dedicated index.
	•	Build and export Kibana dashboards (Top Attacker IPs, Alerts Over Time).

Phase 2 – Add More Log Sources (In Progress)
	•	Windows logs via Winlogbeat or Sysmon.
	•	Web server logs with Filebeat.
	•	Simulated firewall logs.

Phase 3 – Expand Detection Rules (Planned)
	•	Windows failed login thresholds.
	•	Windows persistence (new user created).
	•	Web reconnaissance (multiple 404s).
	•	Firewall port scans.

Phase 4 – Additional Dashboards (Planned)
	•	Windows dashboard.
	•	Web dashboard.
	•	Firewall dashboard.
	•	Combined security overview.

Phase 5 – Case Study Documentation (Planned)
	•	Walkthroughs of simulated incidents.
	•	Example SOC response workflows.

Phase 6 – Threat Intelligence Enrichment (Planned)
	•	Integration with AlienVault OTX or AbuseIPDB.
	•	Tag alerts with known malicious indicators.

Phase 7 – AI and Emerging Threats (Planned)
	•	Ingest logs related to AI systems (e.g., prompt injection attempts, API misuse).
	•	Simulate AI-powered attacks such as automated phishing or credential stuffing with LLMs.
	•	Experiment with anomaly detection using machine learning or AI-assisted correlation.
	•	Build dashboards that track AI-related incidents.
	•	Document case studies of AI attack simulation and detection.

⸻

Learning Outcomes

This project demonstrates:
	•	Building and managing a SIEM pipeline.
	•	Configuring log collection with Filebeat.
	•	Writing parsing and aggregation rules in Logstash.
	•	Generating synthetic attack data for testing.
	•	Creating dashboards and alerts in Kibana.
	•	Documenting the growth of a SIEM through iterative phases.
	•	Considering AI-related threats and modern detection strategies.

⸻

Notes
	•	This lab is intended for educational and demonstration purposes.
	•	The pipeline can be extended to other log sources and detection use cases.
	•	Dashboards and exports are included for reproducibility.