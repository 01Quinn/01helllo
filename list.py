#1
dice = int(input("how many dice do you want to roll? "))

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


