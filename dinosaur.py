import time
from time import sleep
import random

class Dinosaur:
    def __init__(self, name, attack_power, health, speed, defense):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.speed = speed
        self.defense = defense
        self.initiative = 0

    def attack(self, targets):
        target = random.choice(targets)
        print(f'{self.name} hits {target.name} for {self.attack_power} damage!')
        target.health -= self.attack_power
        # sleep(.4)
        if target.health > 0:
            print(f'{target.name} has {target.health} health remaining!')
        else:
            print(f'{target.name} has no remaining health!')
        return target

