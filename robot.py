from weapon import Weapon
import time
from time import sleep

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Beam Sword', 45)

    def attack(self, dinosaur):
        print(f'{self.name} hits {dinosaur.name} for {self.active_weapon.attack_power} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        sleep(.4)
        print()
        if dinosaur.health > 0:
            print(f'{dinosaur.name} has {dinosaur.health} health remaining!')
        else:
            print(f'{dinosaur.name} has no remaining health!')