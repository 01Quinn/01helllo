import math
print("Hello, Quinn")
#1
rds = float(input("Enter rds: "))
area = math.pi * (rds ** 2)
print(area)

#2
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print(f"a is: {b}, b is: {a}.")

#3
length = float(input("Enter a height of a rectangle: "))
width = float(input("Enter a width of a rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"area is {area}, Perimeter is: {perimeter}.")

#4
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a number: "))
sum = a + b + c
average = sum / 3
print(f"The average is: {average}, the sum is: {sum}")

#5
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3
talents = float(input("Enter number of talents: "))
pounds = float(input("Enter number of pounds: "))
lots = float(input("Enter number of lots: "))
sum_pounds = pounds + talents * 20
sum_lots = lots + sum_pounds * 32
grams = float(13.3 * float(sum_lots))
kilograms = float(grams / 1000)
sum_grams = grams % 1000
print(f"The weight in modern units: ")
print(f"{int(kilograms)} kilograms and {sum_grams:.2f} grams")

#6
import random
num1 = int(random.randint(0, 9))
num2 = int(random.randint(0, 9))
num3 = int(random.randint(0, 9))
print(num1, num2, num3)

num4 = int(random.randint(1, 6))
num5 = int(random.randint(1, 6))
num6 = int(random.randint(1, 6))
num7 = int(random.randint(1,  6))
print(num4, num5, num6, num7)