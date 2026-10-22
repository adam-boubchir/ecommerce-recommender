
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "interactions.csv"
OUTPUT_PATH = (
    PROJECT_ROOT / "data" / "processed" / "user_item_scores.csv"
)

# Limiter l'influence des interactions répétées extrêmes.
MAX_SCORE = 10.0


def main():
    print("Chargement des interactions...")
    df = pd.read_csv(
        INPUT_PATH,
        usecols=["visitorid", "itemid", "weight"],
    )

    print("Agrégation par visiteur et produit...")
    scores = (
        df.groupby(["visitorid", "itemid"], as_index=False)["weight"]
        .sum()
        .rename(columns={"weight": "score"})
    )

    scores["score"] = scores["score"].clip(upper=MAX_SCORE)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    scores.to_csv(OUTPUT_PATH, index=False)

    print(f"\nPaires uniques : {len(scores):,}")
    print(f"Score minimum : {scores['score'].min():.1f}")
    print(f"Score maximum : {scores['score'].max():.1f}")
    print(f"Fichier créé : {OUTPUT_PATH}")
    print("\nExemple :")
    print(scores.head().to_string(index=False))


if __name__ == "__main__":
    main()
