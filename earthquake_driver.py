from pathlib import Path
from earthquake_data import EarthquakeData

def main():
    # Path to your jsonfile
    print("See earthquake data")
    file1 = input("Enter path for json file: ").strip()

    #Load Data
    ed1 = EarthquakeData(f"CSV/eq_data/{file1}.geojson")
    ed1.load_data()

    #Plot 
    ed1.plot()
if __name__ == '__main__':
    main()    