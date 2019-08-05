import csv
from math import sin, cos, sqrt, atan2, radians

# Using Python 3.7

def getDistanceFromLatLngInKm(lat1, lng1, lat2, lng2):
    R = 6371  # Radius of the earth in km
  
    lat1 = radians(lat1)
    lng1 = radians(lng1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)

    dLng = lng2 - lng1
    dLat = lat2 - lat1
  
    a = sin(dLat/2)**2 + cos(lat1) * cos(lat2) * sin(dLng/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    d = R * c # Distance in km
    return d


def getColumnsFromFile(file):
    records = []

    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records


def main():

    CargoRecords = getColumnsFromFile('cargo.csv')
    TruckRecords = getColumnsFromFile('trucks.csv')

    CargoOriginLat = float(CargoRecords[0]['origin_lat'])
    CargoOriginLng = float(CargoRecords[0]['origin_lng'])
    TruckLat = float(TruckRecords[0]['lat'])
    TruckLng = float(TruckRecords[0]['lng'])

    # Preset first truck as the closet
    minTruckRecordsIndex = 0
    minTruckToCargoOriginDist = getDistanceFromLatLngInKm(TruckLat, TruckLng, CargoOriginLat, CargoOriginLng)

    for i in range(0, len(CargoRecords)):
        CargoOriginLat = float(CargoRecords[i]['origin_lat'])
        CargoOriginLng = float(CargoRecords[i]['origin_lng'])
        CargoDestinationLat = float(CargoRecords[i]['destination_lat'])
        CargoDestinationLng = float(CargoRecords[i]['destination_lng'])

        # Find truck closet to cargo pickup location
        for j in range(1, len(TruckRecords)):
            TruckLat = float(TruckRecords[j]['lat'])
            TruckLng = float(TruckRecords[j]['lng'])
            TruckToCargoOriginDist = getDistanceFromLatLngInKm(TruckLat, TruckLng, CargoOriginLat, CargoOriginLng)

            if TruckToCargoOriginDist < minTruckToCargoOriginDist:
                minTruckToCargoOriginDist = TruckToCargoOriginDist
                minTruckRecordsIndex = j

        CargoOriginToDestinationDist = getDistanceFromLatLngInKm(CargoOriginLat, CargoOriginLng, CargoDestinationLat, CargoDestinationLng)
        print(f"Cargo Product: {CargoRecords[i]['product']} ---- Truck: {TruckRecords[minTruckRecordsIndex]['truck']} ---- MinTruckToCargoOriginDistance: {minTruckToCargoOriginDist}km ---- CargoOriginToDestinationDistance: {CargoOriginToDestinationDist}km ---- TotalMinDistance: {minTruckToCargoOriginDist + CargoOriginToDestinationDist}km")
        print(f"{TruckRecords.pop(minTruckRecordsIndex)['truck']} Removed")

        # Time Complexity: T(m,n) = O(m(n-1)); Quadratic Time, where m = size of cargo list and n = size of truck list


if __name__ == "__main__": 
    main()
