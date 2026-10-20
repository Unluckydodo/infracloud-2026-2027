import json
from sysinfo_helper import filter_system_info

if __name__ == "__main__":
    resultaat = filter_system_info()
    bestand = "systeeminformatie_windows.json"

    with open(bestand, "w", encoding="utf-8") as f:
        json.dump(resultaat, f, indent=2)
    print(f"Gegevens weggeschreven naar {bestand}")

    with open(bestand, "r", encoding="utf-8") as f:
        print(json.load(f))