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
max_num = None
min_num = None
num1 = (input("Enter a number: "))
while num1 != "":
    num1 = float(num1)
    if max_num is None or num1 > max_num:
        max_num = num1
    if min_num is None or num1 < min_num:
        min_num = num1

    num1 = (input("Enter a number: "))
print(f"Max: {max_num} and Min: {min_num}")

#4
import random
num = random.randint(1, 10)
while True:
    num1 = int(input("Enter a number: "))
    if num > num1:
        print("Too high")
    elif num < num1:
        print("Too low")
    else:
        print("Correct")
        break

#5
round = 0
while round < 5:
    name = input("Enter the username: ")
    password = input("Enter the password: ")
    if name == "python" and password == "rules":
        print(f"Welcome {name}")
        break
    else:
        print("Incorrect username and password, please try again!")
        round += 1
    if round == 5:
        print("Access denied!")

#6
import random
circle = 0
count = 0
num = int(input("Enter how many points to generate: "))
while count < num:
    a = random.uniform(-1, 1)
    b = random.uniform(-1, 1)
    if a ** 2 + b ** 2 < 1:
        circle += 1
    count += 1
c = 4 * circle / num
print(c)

