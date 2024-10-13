# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
import mysql.connector
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'airports',
    user = 'root',
    password = '453489',
    autocommit = True)
print("connection")


def get_airport(area_code):
    sql = (f"SELECT type, count(*) as count "
           f"FROM airport WHERE iso_country = '{area_code}"
           f"group by type, count(*) order by count desc")

    cursor = connection.cursor()
    cursor.execute(sql, area_code)
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
            for type, count in airport_info:
                print(f"\t{type}: {count}")
        else:
            print("No airports found.")
main()


