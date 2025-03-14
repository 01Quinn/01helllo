#1
# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
import random

from list import total_sum


def dice():
    roll = random.randint(1, 6)
    return roll

result = 0
while result != 6:
    result = dice()
    print("Roll:", result)


# 2
# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.
import random
def dice_roll(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("enter number of sides: "))
    attempt = 0
    while True:
        result = dice_roll(sides)
        attempt += 1
        print(f"Roll {attempt}: it is a {result}.")
        if result == sides:
            print("You win!")
            break

main()


#3
# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def converted_to_liters(gallons):
    liters = gallons * 3.785
    return liters


def main():

    while True:
        gallons = float(input("Enter the volume of gasoline in gallons: "))
        if gallons < 0:
            print("Please enter a positive number!")
            break

        liters = converted_to_liters(gallons)
        print(f"The volume of gasoline in liters: {liters}")


main()


# 4
# Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.

def num(mylist):
    total = 0
    for number in (mylist):
        total += number
    return total

mylist = [1, 3, 4, 5]
result = list(num(mylist))
print(result)

# 5
# Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list
# except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original as well as the cut-down list.

def evenlist(numbers):
    evenlist = []
    for number in numbers:
        if number % 2 == 0:
            evenlist.append(number)
        return evenlist

mylist = [2,4,5,6,7,8,9,12]
result = evenlist(mylist)
print(f"Even list: {result}")

# 6
# Write a function that receives two parameters:
# the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
import math
def pizza(diameter,price):
    radius = (diameter / 2) / 100
    area_pizza = math.pi * radius ** 2
    price_meter = price / area_pizza
    return price_meter
pizza1_diameter = float(input("Enter the diameter of the first pizza: "))
pizza1_price = float(input("Enter the price of the pizza: "))
pizza2_diameter = float(input("Enter the diameter of the second pizza: "))
pizza2_price = float(input("Enter the price of the pizza: "))
if pizza(pizza1_diameter, pizza1_price) < pizza(pizza2_diameter, pizza2_price):
    print("The first pizza is a good deal!")
elif pizza(pizza1_diameter, pizza1_price) > pizza(pizza2_diameter, pizza2_price):
    print("The second pizza is a good deal!")
else:
    print("Both pizzas offer the same value!")
