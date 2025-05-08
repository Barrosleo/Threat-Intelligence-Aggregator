from threat_feed_collector import fetch_threat_feeds
from log_collector import load_logs
from correlation_engine import correlate_data
from alert_scoring import score_alerts
from dashboard import create_dashboard
from response_report import generate_report
import os

def main():
    # Ensure required directories exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("docs", exist_ok=True)

    # 1. Collect threat intelligence data
    threat_data = fetch_threat_feeds()
    print("Threat intelligence data collected:", threat_data)

    # 2. Load internal (simulated) logs
    logs = load_logs("data/simulated_logs.csv")
    print("Internal logs loaded:", logs.shape[0], "records")

    # 3. Correlate logs with threat data
    correlated = correlate_data(threat_data, logs)
    print("Correlation complete. Matched events:", correlated.shape[0])

    # 4. Score alerts based on risk
    scored_alerts = score_alerts(correlated)
    print("Alert scoring complete:", scored_alerts)

    # 5. Generate response report (JSON)
    report = generate_report(scored_alerts)
    with open("docs/threat_report.json", "w") as f:
        f.write(report)
    print("Report generated at docs/threat_report.json")

    # 6. Launch the dashboard for visualization
    app = create_dashboard(scored_alerts)
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
