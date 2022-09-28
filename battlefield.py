from dinosaur import Dinosaur
from robot import Robot
import time
from time import sleep
import random
# 
class Battlefield:
    def __init__(self):
        self.robots = []
        self.dinosaurs = []

    def run_game(self):
        self.display_welcome()
        game_selection = self.choose_game_mode()
        if game_selection == '1':
            self.dinosaurs = self.form_team(dinosaurs, 1)
            self.robots = self.form_team(robots, 1)
        else:
            self.dinosaurs = self.form_team(dinosaurs, 3)
            self.robots = self.form_team(robots, 3)
        self.battle_phase(self.dinosaurs, self.robots)
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the war-zone...')
        sleep(1.5)
        print('\nAre you prepared to fight?')
        sleep(1)

    def choose_game_mode(self):
        print('[1] 1v1 Deathmatch\n[2] Team Battle')
        game_mode = input('Select your gamemode: ')
        while game_mode != '1' and game_mode != '2':
            game_mode = input('Invalid selection. Please select 1 or 2: ')
        sleep(.5)
        return game_mode

    def form_team(self, species, team_size):
        team = []
        while len(team) < team_size:
            teammate = random.choice(species)
            if teammate not in team:
                team.append(teammate)
        return team

    # def roll_initiative(self, fighter):
    #     initiative = random.randrange(1, 21) + fighter.speed
    #     return initiative


    def battle_phase(self, dinos, bots):
        round_counter = 0
        all_fighters = list(dinos) + list(bots)
        sleep(2)
        print('Something\'s coming...')
        enemies = ''
        for dino in dinos:
            enemies += f'{dino.name}!'
        sleep(1.5)
        print(enemies)
        sleep(1.5)
        while len(dinos) > 0 and len(bots) > 0:
            round_counter += 1
            print(f'\nRound {round_counter}!\n')
            sleep(1)
            # for fighter in all_fighters:
            #     fighter.initiative = self.roll_initiative(fighter)
            # all_fighters.sort(key=str(fighter.initiative))
            for fighter in all_fighters:
                if isinstance(fighter, Dinosaur):
                    sleep(1.5)
                    print(f'{fighter.name}\'s turn!\n')
                    target = fighter.attack(bots)
                    if target.health <= 0:
                        all_fighters.remove(target)
                        self.robots.remove(target)
                else:
                    sleep(1.5)
                    print(f'{fighter.name}\'s turn!\n')
                    target = fighter.attack(dinos)
                    if target.health <= 0:
                        all_fighters.remove(target)
                        self.dinosaurs.remove(target)


    def display_winner(self):
        if len(self.robots) > 0:
            print('VICTORY!')
        else:
            print('Defeat...')

#################### TEAM BATTLE ####################

    # def form_team(self, species):
    #     team = []
    #     while len(team) > team_size

    # def display_winning_team(self):
    #     pass

###################### LISTS ######################

trike = Dinosaur('Triceratops', 25, 150, 2, 5)
rex = Dinosaur('Tyrannosaurus', 50, 150, 3, 2)
anky = Dinosaur('Ankylosaurus', 40, 100, 1, 5)
ptera = Dinosaur('Pteranadon', 10, 75, 5, 2)
raptor = Dinosaur('Velociraptor', 30, 75, 4, 2)

dinosaurs = [trike, rex, anky, ptera, raptor]

bot1 = Robot('M.R. Combat Golem')
bot2 = Robot('Sanitation Bot 126')
bot3 = Robot('DINO DEFENSE DROID')
bot4 = Robot('L8R-G8R')
bot5 = Robot('The Equalizer')

robots = [bot1, bot2, bot3, bot4, bot5]