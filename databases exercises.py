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
    password = '453489',
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