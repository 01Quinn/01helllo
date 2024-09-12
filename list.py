#1
# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers.
# Use a for loop.
import random
rolls = []
total_sum = 0
dices = int(input("how many dice do you want to roll? "))
for i in range(dices):
    roll = random.randint(1, 6)
    rolls.append(roll)
    total_sum += sum(rolls)
print("Rolls:", rolls)
print("Sum:", total_sum)

#2 Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
numbers = []
while True:
    num = input("enter a number or press enter to quit : ")
    if num == "":
        break
    numbers.append(float(num))
    sorted_numbers = sorted(numbers, reverse=True)
    five_numbers = sorted_numbers[:5]
    print("The five greatest numbers in descending order:")
    for n in five_numbers:
        print(f"The five greatest number are {n}.")

#3
# Write a program that asks the user for an integer and tells if the number is a prime number.
#Prime numbers are number that are only divisible by one or the number itself.
#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
num = int(input("Enter a number: "))
prime_numbers = True
if num <= 1:
    print("The number is not a prime number")
    prime_numbers = False

else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_num = False
            break
if prime_numbers:
    print(f"The number {num} is a prime number")
else:
    print(f"The number {num} is not a prime number")

#4
# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
# and stores them into a list structure. Finally, the program prints out the names of the cities one by one,
# one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.
cities = []
for d in range(5):
    input_city = input("Enter a city: ")
    cities.append(input_city)
for c in cities:
    print(c)




