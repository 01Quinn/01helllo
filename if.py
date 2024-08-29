# ''''''
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

import random
result = random.choice(["heads", "tails"])
while True:
    if result == "heads":
        print("flipped:", result)
        break
    else:
        print("try again")

