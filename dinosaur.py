class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        robot.health = (robot.health - self.attack_power)
        print(f'{self.name} hits {robot.name} for {self.attack_power}damage!')
        if robot.health > 0:
            print(f'{robot.name} has {robot.health} remaining!')
        else:
            print(f'{robot.name} has no remaining health!')