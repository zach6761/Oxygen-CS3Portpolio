class PhysicsInstrument:
    def __init__(self, name, measurement):
        self.name = name
        self.__measurement = measurement

    def get_measurement(self):
        return self.__measurement

    def display_reading(self):
        print(f"{self.name}: {self.get_measurement()}")


class Thermometer(PhysicsInstrument):
    def __init__(self, temperature):
        super().__init__("Thermometer", temperature)

    def display_reading(self):
        temperature = self.get_measurement()

        if temperature < 20:
            condition = "Cool Temperature"
        elif 20 <= temperature <= 30:
            condition = "Normal Temperature"
        else:
            condition = "High Temperature"

        print(f"Thermometer: {temperature}°C - {condition}")


class Speedometer(PhysicsInstrument):
    def __init__(self, speed):
        super().__init__("Speedometer", speed)

    def display_reading(self):
        print(f"Speedometer: {self.get_measurement():.2f} km/h")


class ForceMeter(PhysicsInstrument):
    def __init__(self, force):
        super().__init__("Force Meter", force)

    def display_reading(self):
        print(f"Force Meter: {self.get_measurement():.2f} N")


# User input
temperature = float(input("Enter the temperature in Celsius: "))
thermometer = Thermometer(temperature)

distance = float(input("Enter the distance traveled in kilometers: "))
time = float(input("Enter the time taken in hours: "))

if time > 0:
    speed = distance / time
    speedometer = Speedometer(speed)
    speed_valid = True
else:
    print("Invalid time! Please enter a value greater than zero.")
    speed_valid = False

mass = float(input("Enter the mass of the object in kilograms: "))
acceleration = float(input("Enter the acceleration in meters per second squared: "))
force = mass * acceleration
force_meter = ForceMeter(force)

# Demonstrate polymorphism
results = [thermometer]
if speed_valid:
    results.append(speedometer)
results.append(force_meter)

print("\nPhysics Results")
print("-" * 30)
for item in results:
    item.display_reading()
