from weapon import Weapon
import time
from time import sleep

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = self.weapon_selection

    def weapon_selection(self):
        print('Select your weapon!')
        weapon_number = 1
        for weapon in weapons:
            print (f'{weapon_number}: {weapon.name} [{weapon.attack_power}]')
            weapon_number += 1
        user_selection = int(input('Enter 1, 2, or 3 to select: '))
        while user_selection is not 1 and user_selection is not 2 and user_selection is not 3:
            user_selection = int(input('Invalid entry, please only enter 1, 2, or 3: '))
        weapon_index = user_selection - 1
        chosen_weapon = weapons[weapon_index]
        return chosen_weapon

    def attack(self, dinosaur):
        self.active_weapon = self.weapon_selection()
        print(f'{self.name} hits {dinosaur.name} for {self.active_weapon.attack_power} damage!')
        dinosaur.health -= self.active_weapon.attack_power
        # sleep(.4)
        if dinosaur.health > 0:
            print(f'{dinosaur.name} has {dinosaur.health} health remaining!')
        else:
            print(f'{dinosaur.name} has no remaining health!')


sword = Weapon('Energy Sword', 40)
rifle = Weapon('Beam Rifle', 30)
shotgun = Weapon('Shotgun', 50)

weapons = [rifle, sword, shotgun]
