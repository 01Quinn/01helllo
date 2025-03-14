# 1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location
# (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = '00000',
    autocommit = True)
print("connection")

def get_airport(icao_code):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql,(icao_code,))
    result = cursor.fetchone()
    return result


def main():
    while True:
        icao_code = input("Enter the ICAO code of the airport or quit(q): ")

        if icao_code.lower() == 'q':
            print("Exiting the program...")
            break

        airport_info = get_airport(icao_code)

        if airport_info:
            name, municipality = airport_info
            print(f"Airport name: [{name}]")
            print(f"Airport location: {municipality}")
        else:
            print(f"Airport not found")


main()


# 2
import mysql.connector
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = '00000',
    autocommit = True)
print("Connection established.")


def get_airport(area_code):
    sql = (f"SELECT name, type "
           f"FROM airport WHERE iso_country = %s "
           f" order by type")

    cursor = connection.cursor()
    cursor.execute(sql, (area_code,))
    result = cursor.fetchall()
    return result


def main():
    while True:
        area_code = input("Enter the area code (e.g., FI) or 'q' to quit: ")
        if area_code == 'q':
            print("Bye")
            break

        airport_info = get_airport(area_code)

        if airport_info:

            print(f"Airport in {area_code}:")
            for airport_type, name in airport_info:
                print(f"\t{airport_type}: {name}")
        else:
            print("No airports found.")


main()


# 3
import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = '000000',
    autocommit = True)
print("connection")


def get_airport_coordinates(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def calculate_distance(icao_code1, icao_code2):
    coordinates1 = get_airport_coordinates(icao_code1)
    coordinates2 = get_airport_coordinates(icao_code2)

    if coordinates1 is None or coordinates2 is None:
        return None

    distance = geodesic(coordinates1, coordinates2).kilometers
    return distance


def main():
    while True:
        icao_code1 = input("Enter the ICAO code of the first airport: ")

        if icao_code1.lower() == 'q':
            print("Exiting the program...")
            break
        icao_code2 = input("Enter the ICAO code of the second airport: ")

        distance = calculate_distance(icao_code1, icao_code2)

        if distance is not None:
            print(f"The distance between the two airports is {distance:.2f} kilometers.")
        else:
            print("Error. Please check the ICAO codes and try again.")


main()

