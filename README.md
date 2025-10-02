SIEM Home Lab

This repository contains a home lab environment for building a Security Information and Event Management (SIEM) platform using the Elastic Stack (Elasticsearch, Logstash, Kibana) with Filebeat. The project demonstrates log collection, parsing, and visualization of security events, focusing on detecting SSH brute-force attacks.

⸻

Overview

The lab includes:
	•	A Docker-based Elastic Stack (Elasticsearch, Logstash, Kibana).
	•	Filebeat integration for log shipping.
	•	A custom Logstash pipeline for parsing syslog and SSH events.
	•	A Python log generator to simulate brute-force attempts.
	•	Exported Kibana dashboards to visualize alerts.

⸻

Repository Structure
	•	docker-compose.yml – starts Elasticsearch, Logstash, and Kibana containers.
	•	configs/logstash/pipeline/logstash.conf – defines the Logstash pipeline for syslog parsing.
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
	4.	Update the Filebeat configuration at /opt/homebrew/etc/filebeat/filebeat.yml:
filebeat.inputs:
	•	type: log
enabled: true
paths:
	•	/var/log/*.log
	•	/private/var/log/*.log
tags: [“macos”,“syslog”]
output.logstash:
hosts: [“localhost:5514”]
	5.	Start Filebeat:
brew services start filebeat
	6.	Generate test logs:
python3 scripts/generate_syslog.py
	7.	Access Kibana at:
http://localhost:5601

⸻

Dashboards and Alerts

A Kibana dashboard is included to visualize SSH brute-force alerts.

Visualizations
	•	Top Attacker IPs – displays the source IPs responsible for failed SSH login attempts.
	•	Alerts Over Time – shows the frequency of brute-force attempts across a time range.

Import Instructions
	1.	In Kibana, navigate to:
Stack Management > Saved Objects > Import
	2.	Select the file:
dashboards/ssh_bruteforce_dashboard.ndjson
	3.	If prompted with a Data View Conflict:
	•	Associate with the data view for alerts-ssh-*
	•	Confirm that the timestamp field is set to @timestamp

Usage
	•	Open the dashboard titled SSH Brute-Force Alerts
	•	Adjust the time range (for example: Last 15 minutes or Last 1 hour)
	•	Run the log generator to simulate new alerts
	•	Refresh the dashboard to observe updates

⸻

Learning Outcomes

This project demonstrates the following skills:
	•	Building and managing a SIEM pipeline
	•	Configuring log collection with Filebeat
	•	Writing Logstash parsing rules
	•	Generating synthetic attack data for testing
	•	Creating and exporting detection dashboards in Kibana

⸻

Notes
	•	This lab is intended for educational and demonstration purposes.
	•	The detection pipeline can be extended to support additional log sources such as web server logs or Windows event logs.
	•	The exported Kibana dashboard is included for reproducibility.