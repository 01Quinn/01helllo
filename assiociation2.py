from assiociation import Car
import random


class ElectricCar(Car):
    def __init__(self, license, maximum_speed, capacity):
        super().__init__(license, maximum_speed)
        self.capacity = capacity

class GasolineCar(Car):
    def __init__(self, license, maximum_speed, volume):
        super().__init__(license, maximum_speed)
        self.volume = volume

ecar = ElectricCar(license='ABC-15', maximum_speed=180, capacity=52.5)
gcar = GasolineCar("ACD-123", 165, 32.3)

for car in [ecar, gcar]:
    if hasattr(car, 'capacity'):
        car.capacity = car.maximum_speed

    if hasattr(car, 'volume'):
        car.volume = car.maximum_speed



    print("---------------------")
    print(f"Car {car.registration_number}, maximum speed {car.maximum_speed}km/h, volume {car.volume}\n"
          f"Current speed {car.current_speed}km/h,")

car.accelerate(random.randint(10,100))
car.drive(random.randint(1,10))

print(ecar.maximum_speed)
print(ecar.current_speed)
print(ecar.travelled_distance)
ecar.accelerate(50)
ecar.drive(4)
print(ecar.capacity)
print(ecar.current_speed)
print(ecar.travelled_distance)

