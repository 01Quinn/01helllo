#1
# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
import random


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


# 5

