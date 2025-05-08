import pandas as pd

def correlate_data(threat_df, logs_df):
    # For simplicity, assume logs have an 'ip' column and threat_df has an 'indicator' where type is IP.
    ip_threats = threat_df[threat_df["type"] == "IP"]
    if logs_df.empty or ip_threats.empty:
        return pd.DataFrame()
    
    # Perform a simple inner join on the IP addresses (indicator vs. ip)
    correlated = pd.merge(logs_df, ip_threats, how="inner", left_on="ip", right_on="indicator")
    return correlated

if __name__ == '__main__':
    # Example usage (requires proper CSV in data/)
    import os
    from log_collector import load_logs
    from threat_feed_collector import fetch_threat_feeds
    logs = load_logs("data/simulated_logs.csv")
    threat_data = fetch_threat_feeds()
    correlated = correlate_data(threat_data, logs)
    print("Correlated data:")
    print(correlated)
