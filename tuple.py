#1
def season(month):
    seasons = ("winter", "spring", "summer", "autumn")

    if month in (12, 1, 2):
        return seasons[0]

    elif month in (3, 4, 5):
        return seasons[1]

    elif month in (6, 7, 8):
        return seasons[2]

    elif month in (9, 10, 11):
        return seasons[3]

    else:
        return 'Invalid month'


input_month = int(input("Please enter a number of a month: "))
input_season = season(input_month)
print(f"The number of the month is {input_month}, {input_season}.")

input_months = []
while True:
    global month
    input_month = input("Please enter a number of a month: ")
    if input_month == "" or input_month == "0":
        break

    input_month = int(input_month)
    input_months.append(input_month)

    for month in input_months:
        input_season = season(month)
    print(f"The number of the month is {month}, {input_season}.")

print("Input stopped")

# 2
names = set()
while True:
    input_name = input("Please enter a name: ")
    if input_name == "":
        print("Invalid name")
        break
    elif input_name in names:
        print("Existing name")
    else:
        print("New name")

    names.add(input_name)

print("List of names:")
for n in names:
    print(n)

# 3
codes = {}
while True:
    new_airport = input("Do you want to enter a new airport(enter 1),"
                        "fetch the information of an existing airport(enter 2), "
                        "or quit( enter q):")

    if new_airport == "q":
        print("Execution ends.")
        break

    elif new_airport == "1":
        ICAO_code = input("Please enter the ICAO code: ")
        airport_name = input("Please enter a name of an airport: ")
        codes[ICAO_code] = airport_name
        print(f"New airport added: {ICAO_code} - {airport_name}")

    elif new_airport == "2":
        ICAO_code = input("Please enter the ICAO code: ")

        if ICAO_code in codes:
            airport_name = codes[ICAO_code]
            print(f"Airport found: {ICAO_code} - {airport_name}")
        else:
            print("Airport not found.")
    else:
        print("Invalid input. Please try again.")

