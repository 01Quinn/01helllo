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

# class Dog:
#     count = 0
#
#
#     def __init__(self, name, age):  # constructor
#         self.name = name
#         self.age = age
#         Dog.count += 1
#
    # setter and getter to manipulate
    #
    # def change_name(self, name):
    #     self.name = name
    #
    # def get_age(self, age):
    #     return self.age
    #
    # def __str__(self):
    #     return f'{self.name} {self.age}'
#
#
# mydog = Dog("chiko", 3)
# yourdog = Dog("chi", 2)
# hisdog = Dog("snowy", 4)
#
# print(mydog.name, mydog.age)
# mydog.change_name("miiko")
# yourdog.change_name("mikko")
#
# print(mydog.name, mydog.age)
# print(str(mydog)) # convert the content to string
# print(str(Dog.count))

import random


class Car:

    def __init__(self, registration_number1, maximum_speed1):
        self.registration_number1 = registration_number1
        self.maximum_speed1 = maximum_speed1
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change1):
        acc_speed = self.current_speed + speed_change1
        if acc_speed < 0:
            self.current_speed = 0
        elif acc_speed > self.maximum_speed1:
            self.current_speed = self.maximum_speed1
        else:
            self.current_speed = acc_speed

    def drive(self, hours):
        new_distance = self.current_speed * hours
        self.travelled_distance += new_distance


car_objects = []
for c in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = f"ABC-{c}"
    car = Car(registration_number, maximum_speed)
    car_objects.append(car)

race_finished = False
hour = 1

while not race_finished:
    print(f"Hour{hour} of the race: ")
    for car in car_objects:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        print(f"Registration number is: {car.registration_number1}.")
        print(f"Maximum speed is: {car.maximum_speed1} km/h.")
        print(f"Current speed is: {car.current_speed} km/h.")

        if car.travelled_distance >= 10000:
            race_finished = True
            break
    hour += 1

print("Final results: ")
print("Registration number | Maximum speed | Current speed | Travelled distance")

for car in car_objects:
    print(f"\t\t{car.registration_number1}\t\t\t{car.maximum_speed1}km/h"
          f"\t\t\t{car.current_speed}km/h\t\t\t\t{car.travelled_distance}km")