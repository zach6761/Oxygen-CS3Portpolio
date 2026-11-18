class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You regain 30 MP!")

class SpeedBoost:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

health_potion = HealthPotion()
mana_potion = ManaPotion()
speed_boost = SpeedBoost()

apply_item(health_potion)  # Output: You regain 50 HP!
apply_item(mana_potion)    # Output: You regain 30 MP!
apply_item(speed_boost)    # Output: Your speed increases for 10 seconds!