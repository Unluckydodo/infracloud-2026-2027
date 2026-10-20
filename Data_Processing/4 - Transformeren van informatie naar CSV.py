import csv
from sysinfo_helper import filter_system_info

if __name__ == "__main__":
    resultaat = filter_system_info()
    bestand = "systeeminformatie_windows.csv"
    kolomnamen = list(resultaat.keys())
    rij = {k: ("N/A" if v is None else v) for k, v in resultaat.items()}

    with open(bestand, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=kolomnamen)
        writer.writeheader()
        writer.writerow(rij)
    print(f"Gegevens weggeschreven naar {bestand}")

    with open(bestand, "r", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            print(dict(row))