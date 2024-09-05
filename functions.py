#3
max_num = None
min_num = None
while True:
    num1 = float(input("Enter a number: "))
    if num1 == " ":
        break
    if max_num is None or num1 > max_num:
        max_num = num1
    print(min_num)
    if min_num is None or num1 < min_num:
        min_num = num1
    print(max_num)



