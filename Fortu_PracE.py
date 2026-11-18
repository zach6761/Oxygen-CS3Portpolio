#creates a parent class called "PhysicsInstrument"
class PhysicsInstrument:
    def __init__(self, name, measurement):
        self.name = name
        self.__measurement = measurement

    def get_measurement(self):
        return self.__measurement

    def display_reading(self):
        print(f"{self.name}: {self.get_measurement()}")

#creates a child class called "Thermometer" which inherits from PhysicsInstrument.
class Thermometer(PhysicsInstrument):
    def __init__(self, temperature):
        super().__init__("Thermometer", temperature)

    def display_reading(self):
        temperature = self.get_measurement()
    #uses the getter method to access the private attribute __measurement and assigns it to temperature.

        if temperature < 20:
            condition = "Cool Temperature"
        elif 20 <= temperature <= 30:
            condition = "Normal Temperature"
        else:
            condition = "High Temperature"

        print(f"Thermometer: {temperature}°C - {condition}")
#here, conditional statements are used to determine whether the temperature is cool, normal, or high, with the unit for Celsius.

#a child class called Speedometer inherits from PhysicsInstrument.
class Speedometer(PhysicsInstrument):
    def __init__(self, speed):
        super().__init__("Speedometer", speed)

    def display_reading(self):
        print(f"Speedometer: {self.get_measurement()} km/h")
#uses the getter method to access the private attribute __measurement, with the unit km/h.

#a child class called ForceMeter inherits from PhysicsInstrument.
class ForceMeter(PhysicsInstrument):
    def __init__(self, force):
        super().__init__("Force Meter", force)

    def display_reading(self):
        print(f"Force Meter: {self.get_measurement()} N")
#using the getter method to access the private attribute __measurement, with the unit N (Newtons).


#user input
temperature = float(input("Enter the temperature in Celsius(number only; no unit): "))
thermometer = Thermometer(temperature)
#asks the user to input temperature and returns the result in Celsius with the right condition.

distance = float(input("Enter the distance traveled in kilometers(number only; no unit): "))
time = float(input("Enter the time taken in hours(number only; no unit): "))
#asks the user to input distance and time, which will be used to calculate speed in km/h.

if time > 0:
    speed = distance / time
    speedometer = Speedometer(speed)
    speed_valid = True
else:
    print("Invalid time! Please enter a value greater than zero.")
    speed_valid = False
#this formula calculates for speed by taking the distance and time entered by the user. this also includes a conditional else statement in case the speed entered is less than zero.

#asks the user to input the mass and accceleration of the object which will be used to calculate force.
mass = float(input("Enter the mass of the object in kilograms(number only; no unit): "))
acceleration = float(input("Enter the acceleration in meters per second squared(number only; no unit)   : "))
force = mass * acceleration
force_meter = ForceMeter(force)
#uses force = ma to calculate the force.


# Demonstrate polymorphism
results = [thermometer]
if speed_valid:
    results.append(speedometer)
results.append(force_meter)

print("\nPhysics Results")
print("===============================")
for item in results:
    item.display_reading()