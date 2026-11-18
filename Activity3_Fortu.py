class Warrior():
    def special_move(self):
        print("Warrior swings a powerful sword!")

class Mage():
    def special_move(self):
        print("Mage casts a powerful spell!")

class Archer():
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

warrior1 = Warrior()
mage1 = Mage()
archer1 = Archer()

warrior1.special_move()
mage1.special_move()
archer1.special_move()

characters = [warrior1, mage1, archer1]
for character in characters:
    perform_move(character)
    