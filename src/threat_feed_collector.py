import pandas as pd
import random

def fetch_threat_feeds():
    # Simulated threat intelligence data from multiple sources
    # In a real scenario, you might use requests to fetch data from APIs/endpoints
    data = [
        {"indicator": "192.168.1.100", "type": "IP", "source": "abuse.ch", "confidence": random.randint(50, 100)},
        {"indicator": "malicious.com", "type": "Domain", "source": "VirusTotal", "confidence": random.randint(50, 100)},
        {"indicator": "e99a18c428cb38d5f260853678922e03", "type": "Hash", "source": "MISP", "confidence": random.randint(50, 100)}
    ]
    return pd.DataFrame(data)

if __name__ == '__main__':
    df = fetch_threat_feeds()
    print("Fetched threat feeds:")
    print(df)
