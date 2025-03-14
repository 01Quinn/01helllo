# 1
# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.
class Car:
    def __init__(self, registration_number, maximum_speed):
        self._registration_number = registration_number
        self._maximum_speed = maximum_speed
        self._current_speed = 0
        self._travelled_distance = 0

new_car = Car("ABC-123", 142)
print("All the properties of the new car are:")
print(f"Registration number is: {new_car.registration_number}.")
print(f"Maximum speed is: {new_car.maximum_speed} km/h.")
print(f"Current speed is: {new_car.current_speed} km/h.")
print(f"Travelled distance is: {new_car.travelled_distance} km")


# 2
class Car:
        def __init__(self, registration_number, maximum_speed):
            self._registration_number = registration_number
            self._maximum_speed = maximum_speed
            self._current_speed = 0
            self._travelled_distance = 0


    def accelerate(self, speed_change):
        acc_speed = self._current_speed + speed_change
        if acc_speed < 0:
            self._current_speed = 0
        elif acc_speed > self._maximum_speed:
            self._current_speed = self._maximum_speed
        else:
            self._current_speed = acc_speed

    def drive(self, hours):
        new_distance = self._current_speed * hours
        self._travelled_distance += new_distance

    @property
    def registration_number(self):
        return self._registration_number

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def travelled_distance(self):
        return self._travelled_distance


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("All the properties of the new car are:")
print(f"Registration number is: {new_car.registration_number}.")
print(f"Maximum speed is: {new_car.maximum_speed} km/h.")
print(f"Current speed is: {new_car.current_speed} km/h.")

new_car.accelerate(-200)
print(f"Final speed is: {new_car.current_speed} km/h.")

# 3
class Car:
    def __init__(self, registration_number, maximum_speed):
        self._registration_number = str(registration_number)
        self._maximum_speed = float(maximum_speed)
        self._current_speed = 0.0
        self._travelled_distance = 0.0

    def accelerate(self, speed_change):
        acc_speed = self._current_speed + speed_change
        if acc_speed < 0:
            self._current_speed = 0
        elif acc_speed > self._maximum_speed:
            self._current_speed = self._maximum_speed
        else:
            self._current_speed = acc_speed

    def drive(self, hours):
        new_distance = self._current_speed * hours
        self._travelled_distance += new_distance

    def stop(self):
        self._current_speed = 0

    @property
    def registration_number(self):
        return self._registration_number

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def travelled_distance(self):
        return self._travelled_distance


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("All the properties of the new car are:")
print(f"Registration number is: {new_car.registration_number}.")
print(f"Maximum speed is: {new_car.maximum_speed} km/h.")
print(f"Current speed is: {new_car.current_speed} km/h.")

new_car.accelerate(-200)
print(f"Final speed is: {new_car.current_speed} km/h.")

new_car.drive(1.5)
print(f"Travelled distance is: {new_car.travelled_distance} km.")

# 4
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
    print(f"\t\t{car.registration_number1}\t\t\t{car.maximum_speed1}km/h\t\t\t{car.current_speed}km/h"
          f"\t\t\t\t{car.travelled_distance}km")

