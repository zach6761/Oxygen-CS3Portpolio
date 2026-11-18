# a. Duck typing is another way to achieve polymorphism besides inheritance. The object must have the minimum necessary attributes/methods.
# b. Car needed to have the minimum necessary method, in this case the speak method. 

class Car:
    def move(self):
        print("The car drives on the road.")


class Boat:
    def move(self):
        print("The boat sails on water.")


class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
    vehicle.move()


car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)

# 3. All three classes, while not inheriting from a parent class, works with start_trip() because each class has a move method, an example of duck typing or polymorphism without inheritance.
