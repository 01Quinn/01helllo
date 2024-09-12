# names = ["AB","BC","CD","DE","EF"]
# id(names)
# list1 = ["a", "b", "c", "d"]
# id(list1[3])
# list2[3] = "k"
# id(list1)
# print(len(list1))
#for number in range(1,11):
    # print(number)

# names = []
# name = input(str("Enter names: "))
# name1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# while name != "":
#     names.append(name)
#     name = input("Enter the next name or quit by pressing Enter: ")
#     print(names)
#     if "t" in name:
#         names.remove('t')
#         names.append(name)
#         names.insert(3, "o")
#         names.extend(name1)
#         for n in names:
#             print(f"hello,{n}")
#
# name = input("Enter the next name or quit by pressing Enter: ")
# print(names)

# num = input("Enter a number: ")
# for i in range(1,9,2):
#     print(i)

# num = int(input("Enter a number: "))
# while num > 0:
#     for i in range(1,num+1):
#         if num % 2 == 0:
#             print(f"the number {num} is even!")
#             num = int(input("Enter a number: "))
#         else:
#             print(f"the number {num} is odd!")
#         num = int(input("Enter a number: "))
#         break

while True:
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
