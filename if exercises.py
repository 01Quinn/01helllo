#1
age = int(input("Enter your age: \n"))
if age >= 18:
    print("The medicine is permitted!")
weight = int(input("Enter your weight: \n"))
if 15 <= age < 18 and weight >= 55:
    print("The medicine is permitted!")

#2
score = float(input("Enter your score: \n"))
if score > 90:
    print("your level is A1.")
elif score > 80:
    print("your level is A2.")
elif score > 70:
    print("your level is B1.")
elif score > 60:
    print("your level is B2.")
elif score > 50:
    print("your level is C1.")
elif score >= 35:
    print("your level is C2.")

#3
wheels_number = int(input("Enter your wheels number: \n"))
if wheels_number == 2:
    battery = input("Does it has a battery? (yes=1, no=2): \n")
    if battery == '1':
        print("This is an ebike!")
    else:
        print("This is an bike!")
elif wheels_number == 3:
    print("This is a ticycle!")
elif wheels_number == 4:
    print("This is a car!")

#4
age = int(input("Enter your age: \n"))
if age >= 65:
    print("Your are retired.")
elif age > 18 :
    print("Your are at the working age.")
elif age > 7:
    print("Your are studying.")
elif age < 6:
    print("Your are a child.")