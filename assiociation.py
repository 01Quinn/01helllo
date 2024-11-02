# 1
class Elevator:

    def __init__(self, num_top, num_bottom):
        self.num_top = num_top
        self.num_bottom = num_bottom
        self.new_elevator = num_bottom

    def go_to_floor(self, floor):
        if floor < self.num_bottom or floor > self.num_top:
            print("Error!")
            return
        if floor > self.new_elevator:
            self.floor_up(floor)
        elif floor < self.new_elevator:
            self.floor_down(floor)
        else:
            print(f"The elevator is on {floor}")

    def floor_up(self, floor):
        while self.new_elevator < floor:
            self.new_elevator += 1
            print(f"The elevator is moving from {floor}to the floor{self.new_elevator}")

    def floor_down(self, floor):
        while self.new_elevator > floor:
            self.new_elevator -= 1
            print(f"The elevator is moving from {floor}to {self.new_elevator}")


h = Elevator(6, 1)
target_floor = int(input("Enter the floor: "))
h.go_to_floor(target_floor)

# 2

class Building:
    def __init__(self, num_bottom, num_top, num_elevators):
        self.num_bottom = num_bottom
        self.num_top = num_top
        self.num_elevators = num_elevators
        self.num_elevators = []

        for e in range(num_elevators):
            elevator = Elevator(num_bottom, num_top)
            self.num_elevators.append(elevator)

    def run_elevator(self, number_elevator, destination):
        if number_elevator < 0 or number_elevator >= self.num_elevators:
            print("Error!")
            return

        elevator = self.elevators[number_elevator]
        print(f"The elevator {number_elevator} goes to floor {destination}.")
        elevator.go_to_floor(destination)

print("\n Elevator is in the building are:" )

building = Building(1, 7, 3)
building.run_elevator(1, 5)
building.run_elevator(2, 4)

# 3
class Building:
    def __init__(self, num_bottom, num_top, num_elevators):
        self.num_bottom = num_bottom
        self.num_top = num_top
        self.num_elevators = num_elevators
        self.elevators = []

        for i in range(num_elevators):
            elevator = Elevator(num_bottom, num_top)
            self.elevators.append(elevator)

    def run_elevator(self, number_elevator, destination):
        if number_elevator < 0 or number_elevator >= self.num_elevators:
            print("Error!")
            return

        elevator = self.elevators[number_elevator]
        print(f"The elevator {number_elevator} goes to floor {destination}")
        elevator.go_to_floor(destination)

    def fire_alarm(self):
        print("Fire alarm activated!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.num_bottom)

print("\n Elevator in the building are: ")

building = Building(1, 10, 7)
building.run_elevator(1, 8)
building.fire_alarm()

# 4
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
