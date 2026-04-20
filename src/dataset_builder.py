import pandas as pd
import os

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"
OUTPUT_FILE = os.path.join(PROCESSED_PATH, "final_dataset.csv")

def clean_url(url):
    if pd.isna(url):
        return None
    return str(url).strip().lower()

def load_phishtank():
    print("Loading PhishTank dataset...")
    df = pd.read_csv(os.path.join(RAW_PATH, "phishtank.csv"))

    df = df[["url"]]
    df["label"] = 1

    return df

def load_legitimate():
    print("Loading legitimate URLs...")
    df = pd.read_csv(os.path.join(RAW_PATH, "legitimate.csv"))

    df.columns = ["url"]
    df["label"] = 0

    return df

def main():
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    
    phish_df = load_phishtank()
    legit_df = load_legitimate()

    print("Combining datasets...")
    df = pd.concat([phish_df, legit_df], ignore_index=True)

    print("Cleaning URLs...")
    df["url"] = df["url"].apply(clean_url)
    df = df.dropna()

    print("Removing duplicates...")
    df = df.drop_duplicates(subset=["url"])

    print("Balancing dataset...")
    min_count = df["label"].value_counts().min()
    df = df.groupby("label").sample(min_count, random_state=42)

    print("Final Dataset Statistics:")
    print(df["label"].value_counts())

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Dataset saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
