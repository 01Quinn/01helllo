#1
# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.
import random
rolls = []
dices = int(input("how many dice do you want to roll? "))
for i in range(dices):
    roll = random.randint(1, 6)
    rolls.append(roll)
sum_rolls = sum(rolls)
print("")



#2 Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
n = []
num = int(input("enter a number: "))
while True:
    if num == "":
        break
    else:
        num = int(input("enter a number: "))
        n.append(num)


