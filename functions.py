#3
max_num = None
min_num = None
num1 = float(input("Enter a number: "))
while True:
    if max_num is None or num1 > max_num:
        max_num = num1
    if min_num is None or num1 < min_num:
        min_num = num1
    if num1 == " ":
        break
    num1 = float(input("Enter a number: "))
    print(f"the max_num is {max_num}, the min_num is {min_num}.")


