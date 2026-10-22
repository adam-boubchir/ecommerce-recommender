
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVENTS_PATH = PROJECT_ROOT / "data" / "raw" / "events.csv"


def main():
    print("Chargement du dataset Retailrocket...")
    df = pd.read_csv(EVENTS_PATH)

    print(f"\nDimensions : {df.shape}")
    print(f"Visiteurs uniques : {df['visitorid'].nunique():,}")
    print(f"Produits uniques : {df['itemid'].nunique():,}")

    print("\nRépartition des événements :")
    print(df["event"].value_counts())

    print("\nValeurs manquantes :")
    print(df.isna().sum())

    print("\nAnalyse terminée.")


if __name__ == "__main__":
    main()
