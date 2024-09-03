from scipy.interpolate import insert
from sympy.external.gmpy import remove

# names = ["AB","BC","CD","DE","EF"]
# id(names)
# list1 = ["a", "b", "c", "d"]
# id(list1[3])
# list2[3] = "k"
# id(list1)
# print(len(list1))

names = []
name = input("Enter names: ")
while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")
    print(names)
    if "t" in name:
        names.remove("t")
        names.insert(3, "o")
    name = input("Enter the next name or quit by pressing Enter: ")

    print(names)
