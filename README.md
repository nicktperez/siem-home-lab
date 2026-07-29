# SIEM Home Lab

A reproducible security monitoring lab built with the Elastic Stack to practice log ingestion, detection engineering, alert triage, and incident documentation.

This project reflects how I am extending more than 10 years of IT operations experience into security operations through hands-on work with telemetry, detections, and analyst workflows.

## What the lab demonstrates

- Deploying Elasticsearch, Logstash, and Kibana with Docker Compose
- Shipping host logs with Filebeat
- Parsing and normalizing authentication events in Logstash
- Generating controlled attack telemetry with Python
- Detecting repeated SSH authentication failures with threshold logic
- Separating raw events from alert indices for investigation
- Building Kibana visualizations for alert volume and source analysis
- Testing prompt-injection detection against synthetic LLM activity

## Architecture

```text
Host and synthetic logs
        |
     Filebeat
        |
     Logstash
   parsing + detection
        |
  +-----+----------------+
  |                      |
Raw event indices    Alert indices
  |                      |
  +-------- Kibana ------+
       investigation
```

## Implemented detections

### SSH brute-force activity

The pipeline groups failed SSH login events by source IP. Five or more failures within one minute create an alert in `alerts-ssh-*`, while the underlying events remain available in `syslog-*` for investigation.

### Prompt-injection indicators

A separate pipeline ingests synthetic JSON prompt events and flags patterns associated with instruction override, credential requests, secret extraction, and exfiltration attempts. Suspicious events are written to `alerts-ai-*`.

These detections use intentionally simple threshold and pattern logic so the behavior remains understandable and testable.

## Investigation case study

- [Synthetic SSH brute-force investigation](docs/ssh-brute-force-case-study.md) documents the detection hypothesis, evidence pivots, analyst disposition, and response recommendations.

## Repository layout

```text
configs/
  filebeat/              Log shipping configuration
  logstash/pipeline/     Parsing and detection pipelines
dashboards/              Exported Kibana saved objects
scripts/                 Synthetic security event generators
docker-compose.yml       Local Elastic Stack deployment
```

## Run the lab

### Requirements

- Docker with Docker Compose
- Python 3
- Filebeat
- A local lab environment

### Start the Elastic Stack

```bash
git clone https://github.com/nicktperez/siem-home-lab.git
cd siem-home-lab
docker compose up -d
```

Open Kibana at [http://localhost:5601](http://localhost:5601).

### Generate SSH test events

```bash
python3 scripts/generate_syslog.py
```

Confirm that raw events appear in `syslog-*` and threshold matches appear in `alerts-ssh-*`.

### Import the dashboard

In Kibana, open **Stack Management > Saved Objects > Import** and select:

```text
dashboards/ssh_bruteforce_dashboard.ndjson
```

Associate the import with the appropriate alert data view and use `@timestamp` as the time field.

## Validation workflow

1. Start the stack and confirm all containers are healthy.
2. Verify Filebeat can reach Logstash.
3. Generate a known set of synthetic events.
4. Confirm raw events are indexed.
5. Confirm the detection threshold produces an alert.
6. Review the alert against the source events.
7. Validate the dashboard reflects the test activity.
8. Document unexpected behavior and adjust the pipeline.

## Roadmap

- Windows Event Log and Sysmon ingestion
- Web server and firewall telemetry
- Additional authentication, persistence, reconnaissance, and port-scan detections
- Threat-intelligence enrichment
- Documented incident case studies and response playbooks
- A consolidated security overview dashboard

## Skills demonstrated

Elastic Stack, Filebeat, Logstash, Kibana, Docker, Python, log analysis, detection engineering, alert triage, security monitoring, and technical documentation.

## Responsible use

All attack data in this repository is synthetic and intended for controlled educational environments. Do not run testing activity against systems you do not own or have explicit permission to assess.
\n## License\n\nMIT — see [LICENSE](LICENSE).\n