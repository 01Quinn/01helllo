#1
i = 1
while i < 1000:
    if i % 3 == 0:
        print(i)
    i += 1

#2
num = input("Enter a number: ")
while True:
    if num < 0:
        break
    num = float(input("Enter a number: "))
    if num > 0:
        num1 = float(num * 2.54)
        print(num1)
        num = float(input("Enter a number: "))
    else:
        break


#3
max_num = 0
min_num = 0
num1 = float(input("Enter a number: "))
while num1 > 0:
    if num1 > max_num:
        max_num = num1
        print(max_num)
    num1 = float(input("Enter a number: "))
    if num1 < min_num:
        min_num = num1
        print(min_num)
    if num == " ":
        break

#4
import random
num = random.randint(1, 10)
