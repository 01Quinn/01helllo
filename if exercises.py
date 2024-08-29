#1
age = int(input("Enter your age: \n"))
if age >= 18:
    print("The medicine is permitted!")
weight = int(input("Enter your weight: \n"))
if 15 <= age < 18 and weight >= 55:
    print("The medicine is permitted!")

#2
score = float(input("Enter your score: \n"))
if score > 90:
    print("your level is A1.")
elif score > 80:
    print("your level is A2.")
elif score > 70:
    print("your level is B1.")
elif score > 60:
    print("your level is B2.")
elif score > 50:
    print("your level is C1.")
elif score >= 35:
    print("your level is C2.")

#3
wheels_number = int(input("Enter your wheels number: \n"))
if wheels_number == 2:
    battery = input("Does it has a battery? (yes=1, no=2): \n")
    if battery == '1':
        print("This is an ebike!")
    else:
        print("This is an bike!")
elif wheels_number == 3:
    print("This is a ticycle!")
elif wheels_number == 4:
    print("This is a car!")

#4
age = int(input("Enter your age: \n"))
if age >= 65:
    print("Your are retired.")
elif age > 18 :
    print("Your are at the working age.")
elif age > 7:
    print("Your are studying.")
elif age < 6:
    print("Your are a child.")


# sum = 0
# counter = 1
# while counter < 10:
#     sum = sum + counter
#     print(f"the counter is: {counter} and sum of counter with the sum {sum}")
#     counter = counter + 1

# i = 1
# n = int(input("enter a limit: "))
# while i <= n:
#     if i % 2 == 0:
#         print(f"{i} is an even number")
#
#     else:
#         print(f"{i} is an odd number")
#
#     i = i + 1

# import random
# num1 = random.randint(1, 9)
# num = 0
# while True:
#     num2 = int(input("Enter a number: "))
#     num = num + 1
#     if num1 == num2:
#         print("Number entered is equal to number")
#         break
#     else:
#         print("Try again")
#
# print(f"you have guessed {num} times")

# user_input = " "
# while user_input != "exit":
#     user_input = input("try something (or exit to quit): ")
#     print(user_input)

# import random
# result = random.choice(["heads", "tails"])
# while True:
#     if result == "heads":
#         print("flipped:", result)
#         break
#     else:
#         print("try again")

#nexted loop
# first = 0
# while first < 5:
#     second = 1
#     while second < 5:
#         print(f"{first} time {second} is ", first * second)
#         second += 1
#     first += 1
#     print("all done")

# for i in range(5):
#     print(i)