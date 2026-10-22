
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
EVENTS_PATH = PROJECT_ROOT / "data" / "raw" / "events.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "interactions.csv"

EVENT_WEIGHTS = {
    "view": 1.0,
    "addtocart": 3.0,
    "transaction": 5.0,
}


def main():
    print("Chargement des événements...")
    df = pd.read_csv(
        EVENTS_PATH,
        usecols=["visitorid", "event", "itemid", "timestamp"],
    )

    # Attribuer un poids à chaque interaction.
    df["weight"] = df["event"].map(EVENT_WEIGHTS)

    # Vérifier les événements inconnus avant de continuer.
    if df["weight"].isna().any():
        unknown = df.loc[df["weight"].isna(), "event"].unique()
        raise ValueError(f"Événements inconnus : {unknown}")

    # Conserver les colonnes nécessaires au modèle.
    interactions = df[
        ["visitorid", "itemid", "event", "timestamp", "weight"]
    ].copy()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    interactions.to_csv(OUTPUT_PATH, index=False)

    print(f"\nInteractions préparées : {len(interactions):,}")
    print(f"Fichier créé : {OUTPUT_PATH}")
    print("\nRépartition par événement :")
    print(interactions["event"].value_counts())
    print("\nExemple de lignes :")
    print(interactions.head().to_string(index=False))


if __name__ == "__main__":
    main()
