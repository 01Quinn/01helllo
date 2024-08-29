#1
length = float(input("Enter the length of the zander: "))
if length < 42:
    print("Please release the fish back into the lake!")
    size_limit = length - 42
    print(f"There are {size_limit} below the size limit!")
else:
    print("You got a zander!")

#2
cabin_class = input("Enter the cabin class: ")
if cabin_class == 'LUX':
    print("Upper-deck cabin with a balcony.")
elif cabin_class == 'A':
    print("Above the car deck, equipped with a window.")
elif cabin_class == 'B':
    print("windowless cabin above the car deck.")
elif cabin_class == 'C':
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3
gender = str(input("Enter the gender (m or f): "))
value = int(input("Enter the hemoglobin value (g/l): "))
if gender == 'm':
    if 134 <= value <= 167:
        print("the hemoglobin value is normal.")
    elif value < 134:
        print("The hemoglobin value is low.")
    else:
        print("The hemoglobin value is high.")
elif gender == 'f':
    if 117 <= value <= 155:
        print("the hemoglobin value is normal.")
    elif value < 117:
        print("The hemoglobin value is low.")
    else:
        print("The hemoglobin value is high.")

#4
year = int(input("Enter a year: "))
if year % 400 == 0 and year % 100 == 0:
    print(f"The year {year} is a leap year!")
elif year % 4 == 0:
    print(f"The year {year} is a leap year!")
else:
    print(f"The year {year} is not a leap year!")












