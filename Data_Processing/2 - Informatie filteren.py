from pprint import pprint
from sysinfo_helper import filter_system_info

if __name__ == "__main__":
    resultaat = filter_system_info()
    print("\n--- GEFILTERDE SYSTEEMINFORMATIE ---")
    pprint(resultaat)