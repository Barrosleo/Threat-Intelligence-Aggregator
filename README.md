# Threat Intelligence Aggregator and Correlation Tool

This tool simulates the collection of threat intelligence data from multiple open-source feeds and correlates it with internal logs to detect potential breaches. Key functionalities include data collection, log correlation, alert scoring, and visualization through an interactive dashboard.

## Features
- **Data Collection:** Fetch threat indicators (IPs, domains, hashes) from simulated feeds.
- **Log Correlation:** Match internal log events with threat data.
- **Alert Scoring:** Prioritize matching events based on risk.
- **Visualization:** Interactive dashboard for insights, with a detailed threat report.
- **Automated Reporting:** Generates a JSON report summarizing correlated events.

## Repository Structure
Threat-Intelligence-Aggregator/
├── README.md
├── requirements.txt
├── docs/
│   └── threat_report.json
├── data/
│   └── simulated_logs.csv
└── src/
    ├── main.py
    ├── threat_feed_collector.py
    ├── log_collector.py
    ├── correlation_engine.py
    ├── alert_scoring.py
    ├── dashboard.py
    └── response_report.py

## Usage

1. Use GitHub Codespaces or the web editor.
2. Install dependencies listed in `requirements.txt`.
3. Run the application with:  
   `python src/main.py`
