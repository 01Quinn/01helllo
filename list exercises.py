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

num = int(input("Enter a number: "))
for i in range(1,num+1):
    if num % 2 == 0:
        print(f" the number {i} is even!")
    else:
        print(f" the number {i} is odd!")

