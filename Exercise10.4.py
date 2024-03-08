import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def accelerate(self, change):
        self.speed += change

    def drive(self, hours):
        self.distance += self.speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-20, 20))
            car.drive(1)

    def print_status(self):
        print(f"{'Car Name':<15} {'Distance (km)':<15}")
        for car in self.cars:
            print(f"{car.name:<15} {car.distance:<15}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

# Create cars for the race
cars = [Car(f"Car {i}", random.randint(100, 200)) for i in range(1, 11)]

# Create a race
grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars)

# Simulate the race progress
hour = 1
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    if hour % 10 == 0:
        print(f"\nRace status after {hour} hours:")
        grand_demolition_derby.print_status()
    hour += 1

print("\nRace finished!")
print("Final Race Status:")
grand_demolition_derby.print_status()
