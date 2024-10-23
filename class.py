# class Dog:
#     pass
# we create a mydog object, constructor
# my_dog = Dog()
# my_dog.name = "Chicko"
# my_dog.age = 2
# print(my_dog.name)
# print(my_dog.age)
#
# your_dog = Dog()
# your_dog.name = "Chi"
# your_dog.age = 3
# print(your_dog.name)
# print(your_dog.age)

class Dog:
    count = 0


    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        Dog.count += 1

    # setter and getter to manipulate

    def change_name(self, name):
        self.name = name

    def get_age(self, age):
        return self.age

    def __str__(self):
        return f'{self.name} {self.age}'


mydog = Dog("chiko", 3)
yourdog = Dog("chi", 2)
hisdog = Dog("snowy", 4)

print(mydog.name, mydog.age)
mydog.change_name("miiko")
yourdog.change_name("mikko")

print(mydog.name, mydog.age)
print(str(mydog)) # convert the content to string
print(str(Dog.count))