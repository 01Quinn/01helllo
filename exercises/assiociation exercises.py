# class Employee:
#     def __init__(self, first_name, last_name):
#         Employee.employee_number = Empolyee.employee_number +1
#         self.employee_number = Employee.employee_number
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_information(self):
#         print(f"Employee {self.first_name}")
#
# class HourlyPaid(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
#
#     def print_information(self):
#
#         print(f"hourly paid {self.salary}")
#         print(f"- Benefits: {self.benefits}")
#
#     def can_use_lounge(self):
#         return False
#
# class Monthly_Paid(Employee):
#     def __init__(self, first_name, last_name, salary, benefits):
#         super().__init__(first_name, last_name)
#         self.monthly_salary = salary
#         self.benefits = benefits
#         self.hourly_salary = salary
#
#
#     def use_benefits(self):
#         print(f"{self.benefits} uses benefits {self.benefits}")
#
# employee1 = Employee("Juha", "T")
# employee1.print_information()
#
# employee2.Hourly_Paid("John", 1200)
# employee2.print_information()
#
# employee3 =Monthly_Paid("Peter", 1200, "Benefits")
#
# employee4 = Monthly_Paid("Anna", Employee2.Hourly_Paid * 80, "healthcare")
#
# for employee in [employee1, employee2, employee3]:
#     employee.print_information()
#
from jedi.debug import speed
from requests.packages import target


# class Vehicle:
#     def __init__(self,speed):
#         self.speed = speed
#         print(f"Vehicle speed {self.speed} km/h")
#
#
# class SportsItem:
#     def __init__(self):
#         print("is a sports item")
#         self.weight = weight
#
#     def is_sport_item(self):
#         return True
#
# class Bycycle(Vehicle, SportsItem):
#     def __init__(self, speed, weight):
#         super().__init__(self, speed, weight)
#         SportsItem.__init__(self, weight)
#
#
#     def print(self):
#
#
# bike = Bicycle
# print(bike.is_sport_item(SportsItem()))

# class Storage:
#     def __init__(self):
#         self.file = []
#
#     def add_file(self, file):
#         self.file.append(file)
#
#     def list_files_in_storage(self):
#         for file in self.file:
#             print(file)
#
# class Camera:
#     def take_photo(self):
#         print('Taking photo')
#         self.photo = "my photo"
#
# class Gps:
#     lat = 61
#     lon = 20
#
# class Call:
#     def dial(self, to_number):
#         for number in to_number:
#             print(f'Dialing {to_number}')
#
#     def make_call(self, to_number):
#         self.dial(to_number)
#         print(f'Calling {to_number}')
#
# class Phone:
#     def __init__(self, brand, model,price):
#         storage.__init__(self)
#         self.brand = brand
#         self.price = price
#         self.model = model
#
#     def print_details(self):
#         print(self.brand, self.model, self.price)
#
# class Laptop(Storage, Camera):
#     def __init__(self):
#         Storage.__init__(self)
#         Camera.__init__(self)
#
#         print("laptop")
#
#
# phone1 = Phone('Bob', 100)
# phone2 = Phone('Alice', 100)
# phone3 = Phone('Bob', 100)
# phone.print_details()
# phone.add_file
# phone.take_photo
# print(phone.photo)
# phone.make
# print(phone.lat)
# print(phone.lon)
#
#
#
# laptop = Laptop()
# laptop.add_file(excel.xlx)

# class Elevator:
#
#     def __init__(self, num_top, num_bottom):
#         self.num_top = num_top
#         self.num_bottom = num_bottom
#         self.new_elevator = num_bottom
#
#     def go_to_floor(self, floor):
#         if floor < self.num_bottom or floor > self.num_top:
#             print("Error!")
#             return
#         if floor > self.new_elevator:
#             self.floor_up(floor)
#         elif floor < self.new_elevator:
#             self.floor_down(floor)
#         else:
#             print(f"The elevator is on {floor}")
#
#     def floor_up(self, floor):
#         while self.new_elevator < floor:
#             self.new_elevator += 1
#             print(f"The elevator is moving from {floor}to the floor{self.new_elevator}")
#
#     def floor_down(self, floor):
#         while self.new_elevator > floor:
#             self.new_elevator -= 1
#             print(f"The elevator is moving from {floor}to {self.new_elevator}")
#
#
# h = Elevator(6, 1)
# target_floor = int(input("Enter the floor: "))
# h.go_to_floor(target_floor)

import random


class Car:
    def __init__(self, registration_number1, maximum_speed1):
        self.registration_number = registration_number1
        self.maximum_speed = maximum_speed1
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        acc_speed = self.current_speed + speed_change
        if acc_speed < 0:
            self.current_speed = 0
        elif acc_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = acc_speed

    def drive(self, hours):
        new_distance = self.current_speed * hours
        self.travelled_distance += new_distance


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for a in self.cars:
            speed_change = random.randint(-10, 15)
            a.accelerate(speed_change)
            a.drive(1)

    def print_status(self):
        print(self.name + ":")
        print("Current status of each car is: ")
        print("Registration number | Maximum speed | Current speed | Travelled distance")

        for b in self.cars:
            print(f"\t\t{b.registration_number}\t\t\t{b.maximum_speed}km/h\t\t\t{b.current_speed}km/h\t\t\t\t{b.travelled_distance}km")

    def race_finished(self):
        for d in self.cars:
            if d.travelled_distance >= self.distance:
                return True
        return False


car_objects = []
for c in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = f"ABC-{c}"
    car = Car(registration_number, maximum_speed)
    car_objects.append(car)

race = Race("Grand Demolition Derby", 8000, car_objects)
hour = 1

while not race.race_finished():
    race.hour_passes()
    if hour % 10 == 0:
        race.print_status()
        print(f"after {hour} hours")
    hour += 1

print("Final results:")
race.print_status()