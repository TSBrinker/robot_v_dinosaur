from weapon import Weapon
import time
from time import sleep

class Robot:
    def __init__(self, name):
        self.name = name
        self.initiative = 0
        self.health = 100
        self.active_weapon = self.weapon_selection
        self.speed = 0

    def weapon_selection(self):
        print('Select your weapon!')
        weapon_number = 1
        for weapon in weapons:
            print (f'{weapon_number}: {weapon.name} [{weapon.attack_power}]')
            weapon_number += 1
        user_selection = int(input('Enter 1, 2, or 3 to select: '))
        while user_selection != 1 and user_selection != 2 and user_selection != 3:
            user_selection = int(input('Invalid entry, please only enter 1, 2, or 3: '))
        chosen_weapon = weapons[user_selection - 1]
        return chosen_weapon

    def target_selection(self, targets): # There's a bug here that if the number of targets is reduced to 2 before all 3 attackers attack, therfore shortening the list, it'll skip ahead before the last attacker can attack
        print('Enemies:')
        i = 1
        for target in targets:
            print(f'[{i}] {target.name} ({target.health} health remaining)')
            i += 1
        target_index = 0
        if len(targets) > 1:
            chosen_target = int(input('Select your target: '))
            while chosen_target > len(targets):
                chosen_target = int(input('Invalid selection, please select a target by number: '))
            target_index = chosen_target - 1
        target = targets[target_index]
        print()
        return target

    def attack(self, targets):
        target = self.target_selection(targets)
        self.active_weapon = self.weapon_selection()
        print(f'{self.name} hits {target.name} for {self.active_weapon.attack_power} damage!')
        target.health -= self.active_weapon.attack_power
        # sleep(.4)
        if target.health > 0:
            print(f'{target.name} has {target.health} health remaining!')
        else:
            print(f'{target.name} has no remaining health!')
        print()
        return target



sword = Weapon('Energy Sword', 40)
rifle = Weapon('Beam Rifle', 30)
shotgun = Weapon('Shotgun', 50)

weapons = [rifle, sword, shotgun]
