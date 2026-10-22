
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "interactions.csv"


def main():
    print("Chargement des interactions...")
    df = pd.read_csv(
        INPUT_PATH,
        usecols=["visitorid", "itemid", "event", "weight"],
    )

    unique_pairs = df[["visitorid", "itemid"]].drop_duplicates()

    print(f"\nNombre d'interactions : {len(df):,}")
    print(f"Paires visiteur-produit uniques : {len(unique_pairs):,}")
    print(f"Interactions répétées au-delà de la première : "
          f"{len(df) - len(unique_pairs):,}")

    print("\nNombre d'interactions par paire :")
    pair_counts = df.groupby(["visitorid", "itemid"]).size()
    print(pair_counts.describe().round(2).to_string())

    print("\nExemple de paires avec plusieurs interactions :")
    repeated = pair_counts[pair_counts > 1].head(10)
    print(repeated.to_string())


if __name__ == "__main__":
    main()
