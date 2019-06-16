import numpy as np
import pandas as pd

print("Loading required data...")
df_raw = pd.read_csv("data/processed/suras.csv")

df = pd.DataFrame()

print("Extracting feature: is_prefix_al...")
df["is_prefix_al"] = df_raw.name.str.startswith("ال")

print("Extracting feature: is_moon...")
suns = [
    "ت", "ث", "د", "ذ", "ر", "ز",
    "س", "ش", "ص", "ض", "ط", "ظ",
    "ل", "ن",
]
moons = [
    "ء", "ا", "آ", "أ", "إ", "ب",
    "ج", "ح", "خ", "ع", "غ", "ف",
    "ق", "ك", "م", "و", "ي", "ه",
    "ة",
]
df["is_moon"] = np.where(
    df.is_prefix_al,
    df_raw.name.str[2],
    df_raw.name.str[0]
)
df.is_moon = np.where(
    df.is_moon.isin(moons),
    "True",
    np.where(
        df.is_moon.isin(suns),
        "False",
        np.nan
    )
)

print("Encoding target: type -> is_meccan...")
df["is_meccan"] = (df_raw.type == "Meccan")

print("Saving to CSV...")
df.to_csv("data/processed/feature.csv", index=False)
