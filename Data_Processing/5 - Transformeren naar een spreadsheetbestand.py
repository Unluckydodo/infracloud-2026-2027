from openpyxl import Workbook
from sysinfo_helper import filter_system_info

if __name__ == "__main__":
    resultaat = filter_system_info()
    bestand = "systeeminformatie_windows.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = "Systeeminformatie"
    ws.append(list(resultaat.keys()))
    ws.append(["N/A" if v is None else v for v in resultaat.values()])

    for kolom in ws.columns:
        breedte = max(len(str(c.value)) for c in kolom) + 2
        ws.column_dimensions[kolom[0].column_letter].width = breedte

    wb.save(bestand)
    print(f"Gegevens weggeschreven naar {bestand}")