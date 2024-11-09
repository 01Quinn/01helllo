import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed = min(self.current_speed + speed_change, self.maximum_speed)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, license_plate, maximum_speed, capacity):
        super().__init__(license_plate, maximum_speed)
        self.capacity = capacity


class GasolineCar(Car):
    def __init__(self, license_plate, maximum_speed, volume):
        super().__init__(license_plate, maximum_speed)
        self.volume = volume


# Creating instances of ElectricCar and GasolineCar
ecar = ElectricCar(license_plate='ABC-15', maximum_speed=180, capacity=52.5)
gcar = GasolineCar(license_plate="ACD-123", maximum_speed=165, volume=32.3)

for car in [ecar, gcar]:
    print("---------------------")
    print(f"Car {car.license_plate}, maximum speed {car.maximum_speed} km/h, "
          f"volume {getattr(car, 'volume', 'N/A')}")
    print(f"Current speed {car.current_speed} km/h.")

    car.accelerate(random.randint(10, 100))
    car.drive(random.randint(1, 10))


print("Final stats for ElectricCar:")
print(f"Maximum speed: {ecar.maximum_speed} km/h")
print(f"Current speed: {ecar.current_speed} km/h")
print(f"Distance travelled: {ecar.travelled_distance} km")
print(f"Battery capacity: {ecar.capacity}")


print("\nFinal stats for GasolineCar:")
print(f"Maximum speed: {gcar.maximum_speed} km/h")
print(f"Current speed: {gcar.current_speed} km/h")
print(f"Distance travelled: {gcar.travelled_distance} km")
print(f"Fuel volume: {gcar.volume} L")