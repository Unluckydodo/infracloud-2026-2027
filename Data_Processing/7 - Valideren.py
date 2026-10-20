import csv
import ipaddress
import os
import re

map_pad = os.path.dirname(os.path.abspath(__file__))
bestand = os.path.join(map_pad, "alle_systeeminformatie.csv")

MAC_PATROON = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$")


def geldig_ip(waarde, versie):
    try:
        return ipaddress.ip_address(waarde).version == versie
    except ValueError:
        return False


def valideer(rij):
    fouten = []

    if not rij["computernaam"] or rij["computernaam"] == "N/A":
        fouten.append("computernaam ontbreekt")

    for veld in ("aantal_fysieke_cpu_cores", "totale_hoeveelheid_ram_gb", "opslagcapaciteit_gb"):
        try:
            if float(rij[veld]) <= 0:
                fouten.append(f"{veld} moet groter dan 0 zijn")
        except (ValueError, TypeError):
            fouten.append(f"{veld} is geen getal")

    if not MAC_PATROON.match(rij["mac_adres_primaire_nic"] or ""):
        fouten.append("ongeldig MAC-adres")
    if not geldig_ip(rij["ipv4_adres_primaire_nic"], 4):
        fouten.append("ongeldig IPv4-adres")
    if rij["ipv6_adres_primaire_nic"] != "N/A" and not geldig_ip(rij["ipv6_adres_primaire_nic"], 6):
        fouten.append("ongeldig IPv6-adres")
    if rij["ipv6_link_local_adres_primaire_nic"] != "N/A" and not geldig_ip(
        rij["ipv6_link_local_adres_primaire_nic"], 6
    ):
        fouten.append("ongeldig IPv6 link-local adres")

    return fouten


if not os.path.exists(bestand):
    print("alle_systeeminformatie.csv bestaat niet. Voer eerst script 6 uit.")
else:
    with open(bestand, "r", encoding="utf-8-sig", newline="") as f:
        for rij in csv.DictReader(f):
            fouten = valideer(rij)
            naam = rij["computernaam"]
            if fouten:
                print(f"[FOUT] {naam}:")
                for fout in fouten:
                    print(f"   - {fout}")
            else:
                print(f"[OK]   {naam}: alle gegevens zijn geldig")