from dinosaur import Dinosaur
from robot import Robot
import time
from time import sleep

class Battlefield:
    def __init__(self):
        self.robot = Robot(gundam)
        self.dinosaur = Dinosaur(triceratops)

    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome...')
        sleep(1)
        print('\nto today\'s battle...')
        sleep(2)
        print('\nROBOT')
        sleep(.25)
        print('\nVERSUS')
        sleep(.25)
        print('\nDINOSAUR!')
        sleep(2)
        print('\nReady?')
        sleep(.4)
        print('\nFIGHT!!')


    def battle_phase(self):
        pass

    def display_winner(self):
        pass

Battlefield.display_welcome(self)
