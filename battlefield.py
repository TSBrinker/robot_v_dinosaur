from dinosaur import Dinosaur
from robot import Robot
import time
from time import sleep
import random

class Battlefield:
    def __init__(self):
        self.robot = Robot('MR Fighting Machine')
        self.dinosaur = Dinosaur('Tina the Trike', 30)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome...')
        sleep(1)
        print('\nto today\'s battle...')
        sleep(2)
        print('\nROBOT')
        sleep(.4)
        print('\nVERSUS')
        sleep(.4)
        print('\nDINOSAUR!')
        sleep(2)
        print('\nReady?')
        sleep(.4)
        print('\nFIGHT!')


    def battle_phase(self):
        round_counter = 0
        while self.dinosaur.health > 0 and self.robot.health > 0:
            round_counter += 1
            print(f'Round {round_counter}!')
            print()
            sleep(.75)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
                print()
            sleep(.5)
            print()
            sleep(.5)
            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)
            print()
            sleep(1)

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f'{self.robot.name} WINS!')
        elif self.robot.health <= 0:
            print(f'{self.dinosaur.name} WINS!')

    def roll_initiative(self):
        initiative = random.randrange(1, 21)
        return initiative