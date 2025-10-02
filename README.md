SIEM Home Lab

This repository contains a home lab setup for building a Security Information and Event Management (SIEM) platform using the Elastic Stack (Elasticsearch, Logstash, Kibana) with Filebeat. It demonstrates how to collect, parse, and visualize security logs — specifically focusing on detecting SSH brute-force attacks.

⸻

🚀 Features
	•	Docker-based ELK stack (Elasticsearch, Logstash, Kibana)
	•	Filebeat integration to ship logs into the pipeline
	•	Custom Logstash pipeline for parsing syslog/SSH events
	•	Python log generator for simulating attacks
	•	Saved Kibana dashboards for visualizing alerts

⸻

📂 Repository Structure
	•	docker-compose.yml → spins up Elasticsearch, Logstash, Kibana
	•	configs/logstash/pipeline/logstash.conf → log parsing pipeline
	•	scripts/generate_syslog.py → sends demo SSH brute-force logs
	•	dashboards/ssh_bruteforce_dashboard.ndjson → exported Kibana dashboard
	•	README.md → project documentation

⸻

🛠 Setup
	1.	Clone this repo and navigate to the project folder.
	2.	Start the Elastic Stack with Docker Compose:
docker compose up -d
	3.	Install Filebeat (on macOS with Homebrew):
brew install filebeat
	4.	Update the Filebeat config (/opt/homebrew/etc/filebeat/filebeat.yml):
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
	7.	Open Kibana at:
http://localhost:5601

⸻

📊 Dashboards & Detections

This lab includes a Kibana dashboard to visualize SSH brute-force alerts in real time.

Visualizations
	•	Top Attacker IPs – top source IPs attempting brute-force SSH logins
	•	Alerts Over Time – a time-series view of alert counts to identify spikes

Import Instructions
	1.	In Kibana, go to:
Stack Management → Saved Objects → Import
	2.	Select the file:
dashboards/ssh_bruteforce_dashboard.ndjson
	3.	If a Data View Conflict appears:
	•	Re-associate with your existing data view for alerts-ssh-*
	•	Ensure the timestamp field is @timestamp

Usage
	•	Navigate to Dashboard → SSH Brute-Force Alerts
	•	Adjust the time range (e.g., Last 15 minutes or Last 1 hour)
	•	Run the log generator again to simulate new attacks
	•	Refresh the dashboard to see alerts populate

⸻

🎯 Learning Objectives

This project is designed to:
	•	Reinforce hands-on SIEM skills
	•	Show practical log collection and parsing
	•	Build detection logic for brute-force attacks
	•	Demonstrate dashboards that highlight security threats

⸻

📌 Notes
	•	This is a home lab setup for educational purposes.
	•	Dashboards and rules can be extended to detect other attacks (web logs, Windows events, etc.).
	•	The exported dashboard is included so others can import and view without recreating manually.