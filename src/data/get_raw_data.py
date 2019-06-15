from xml.dom.minidom import parse

import pandas as pd

names = []
tnames = []
types = []

print("Loading required data...")
dom = parse("data/raw/quran-data_2019-06-15.xml")
suras = dom.getElementsByTagName("sura")
for sura in suras:
    names.append(sura.attributes["name"].value)
    tnames.append(sura.attributes["tname"].value)
    types.append(sura.attributes["type"].value)

print("Saving to CSV...")
df = pd.DataFrame({
    "name": names,
    "tname": tnames,
    "type": types,
})
df.to_csv("data/processed/suras.csv", index=False)
