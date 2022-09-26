from dinosaur import Dinosaur
from robot import Robot
import time
from time import sleep

class Battlefield:
    def __init__(self):
        self.robot = Robot('MR Fighting Machine')
        self.dinosaur = Dinosaur('Tina the Trike', 30)

    def run_game(self):
        self.display_welcome()
        round_counter = 0
        while self.robot.health > 0 and self.dinosaur.health > 0:
            round_counter += 1
            print(f'Round {round_counter}!')
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
        sleep(.5)
        print()
        self.dinosaur.attack(self.robot)
        print()
        sleep(.5)
        self.robot.attack(self.dinosaur)
        print()

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f'{self.robot.name} WINS!')
        elif self.robot.health <= 0:
            print(f'{self.dinosaur.name} WINS!')