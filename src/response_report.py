import json
from datetime import datetime

def generate_report(alerts_df):
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_alerts": int(alerts_df.shape[0]),
        "alerts": alerts_df.to_dict(orient="records")
    }
    return json.dumps(report, indent=4)

if __name__ == '__main__':
    from alert_scoring import score_alerts
    from correlation_engine import correlate_data
    from threat_feed_collector import fetch_threat_feeds
    from log_collector import load_logs

    logs = load_logs("data/simulated_logs.csv")
    threat_data = fetch_threat_feeds()
    correlated = correlate_data(threat_data, logs)
    scored = score_alerts(correlated)
    report = generate_report(scored)
    print(report)
