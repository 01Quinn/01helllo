#1
# def greetings():
#     a = 2
#     b = 3
#     sum = a + b
#     print(f"sum is {sum}")
# greetings()
#
# 2
# def multiply():
#     return 5 * 5
# print(multiply())
# cal = multiply() + 10
# print(cal)

#3
# def sum(a, b):
#     sum = a + b
#     return sum
# print(sum(1,2))
# sum(1, 2)
#
# def subtract(a, b):
#     subtract = a - b
#     if b != 0:
#         return subtract
# print(subtract(1,2))
# subtract(2, 3)
#
#
# def divide(a, b):
#     divide = a / b
#     if b != 0:
#         return divide
# print(divide(2, 3))
# divide(2, 3)
#
#
# def multiply(a, b):
#     multiply = a * b
#     return multiply
# print(multiply(2, 3))
# multiply(2, 3)

#4
# score = []
# def square(number):
#     return number * number
#  while True:
#     n = int(input('Enter a number: '))
#     if n == 0:
#         break
#     else:
#         score.append(n)
# print(f"{n} square :", square(n))
# print("here is the list:")
# print(score)
#
#5
def sum(a,b):
    a = int(input("enter a number: "))
    b = int(input("enter another number: "))
    sum = a+b
    return sum
print(sum(1,2))


n = []
def read():
    while True:
        a = int(input("enter a number: "))
        if a == "":
            break
        else:
           num = a
        a.append(n)
        print(a)

list(n)
print("here is the list:")


def cal_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def find_largest(numbers):
    largest = max(numbers)
    for n in numbers:
        if n > max(numbers):
            largest = max(numbers)
    return largest

import mysql_connector
