#1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

#2
num = float(input("Enter a number of inches: "))
while True:
    if num >= 0:
        num1 = float(num * 2.54)
        print(f"{num} inches equals to {num1} centimeters.")
        num = float(input("Enter a number of inches: "))
    else:
        print("Execution stopped.")
        break

#3
max_num = 0
min_num = 0
num1 = float(input("Enter a number: "))
while num1 > 0:
    if num1 > max_num:
        max_num = num1
        print(num1)
    num1 = float(input("Enter a number: "))
    if num1 < min_num:
        min_num = num1
        print(num1)
    if num == " ":
        break

#4
import random
num = random.randint(1, 10)
num1 = int(input("Enter a number: "))
while True:
    if num > num1:
        print("Too high")
    elif num < num1:
        print("Too low")
    elif num == num1:
        print("Correct")
        break

#5
round_original = 0
while round_original < 5:
    name = input("Enter the username: ")
    password = input("Enter the password: ")
    if name == "python" and password == "rules":
        print(f"Welcome {name}")
        break
    else:
        print("Incorrect username and password, please try again!")
        round_original += 1
    if round_original == 5:
        print("Access denied!")

#6
import random
circle = 0
count = 0
num = int(input("Enter a number: "))
while count < num:
    a = random.randint(-1, 1)
    b = random.randint(-1, 1)
    if a ** 2 + b ** 2 < 1:
    count += 1
    circle += 1
