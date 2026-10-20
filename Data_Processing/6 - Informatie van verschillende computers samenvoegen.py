import csv
import glob
import os

map_pad = os.path.dirname(os.path.abspath(__file__))
bestanden = sorted(glob.glob(os.path.join(map_pad, "systeeminformatie_*.csv")))

alle_rijen = []
kolomnamen = None

for bestand in bestanden:
    with open(bestand, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if kolomnamen is None:
            kolomnamen = reader.fieldnames
        for rij in reader:
            alle_rijen.append(rij)
    print(f"Ingelezen: {os.path.basename(bestand)}")

if not alle_rijen:
    print("Geen systeeminformatie_*.csv bestanden gevonden.")
else:
    uitvoer = os.path.join(map_pad, "alle_systeeminformatie.csv")
    with open(uitvoer, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=kolomnamen)
        writer.writeheader()
        writer.writerows(alle_rijen)
    print(f"{len(alle_rijen)} computer(s) samengevoegd in alle_systeeminformatie.csv")