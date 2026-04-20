import pandas as pd

INPUT_FILE = "data/raw/top-1m.csv"
OUTPUT_FILE = "data/raw/legitimate.csv"

def main():
    df = pd.read_csv(INPUT_FILE, header=None)
    
    # Second column is domain
    df = df[[1]]
    df.columns = ["url"]

    # Add http prefix
    df["url"] = "http://" + df["url"]

    # OPTIONAL: limit size (recommended for balance)
    df = df.sample(50000, random_state=42)

    df.to_csv(OUTPUT_FILE, index=False)

    print("Legitimate dataset created:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
