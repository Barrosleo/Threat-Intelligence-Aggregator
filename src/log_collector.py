import pandas as pd

def load_logs(filepath="data/simulated_logs.csv"):
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Error loading logs from {filepath}: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    logs = load_logs()
    print("Loaded logs:")
    print(logs.head())
