from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Beam Sword', 45)

    def attack(self, dinosaur):
        dinosaur.health = (dinosaur.health - self.active_weapon.attack_power)
        print(f'{self.name} hits {dinosaur.name} for {self.active_weapon.attack_power}damage!')
        if dinosaur.health > 0:
            print(f'{dinosaur.name} has {dinosaur.health} remaining!')
        else:
            print(f'{dinosaur.name} has no remaining health!')