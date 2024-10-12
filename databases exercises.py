# 1
# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location
# (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.
import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = '453489',
    autocommit = True)
print("connection")

def get_airport_coordinates(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
