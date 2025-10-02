# 🛡️ SIEM Home Lab

A hands-on **Security Information & Event Management (SIEM) lab** built with the ELK Stack (Elasticsearch, Logstash, Kibana).  
This project demonstrates **log ingestion, parsing, visualization, and detection engineering** for simulated attacks.

---

## 📖 Project Overview
- **Stack:** Elasticsearch + Logstash + Kibana (Dockerized)  
- **Purpose:** Gain SOC analyst experience by:
  - Ingesting logs (via syslog & agents)
  - Parsing & enriching events
  - Detecting brute-force SSH attempts
  - Visualizing trends and alerts in Kibana
- **Status:** ✅ Basic pipeline working, ingesting simulated SSH brute force attempts

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOURUSERNAME/siem-home-lab.git
cd siem-home-lab
