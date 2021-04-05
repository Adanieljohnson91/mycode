from Character import Character
from random import randint


class Enemy(Character):

    def __init__(self, name, health, strength, defence, wisdom, luck):
        super().__init__(name, health, strength, defence, wisdom, luck)


    def get_health(self):
        return self.health

    def attack(self):
        return self.strength / 10 + randint(0, 1)

    def defend(self):
        return self.defence / 10 + randint(0, 1)

    def takeDamage(self, dmg):
        self.health -= dmg

    def is_alive(self):
        return self.health > 0

class Boss(Enemy):
    def __init__(self, name, health, strength, defence, wisdom, luck):
        super().__init__(name, health, strength, defence, wisdom, luck)

    def attack(self):
        print(self.name + " attacks!")
        return super().attack() + 5
    def takeDamage(self, dmg):
        self.health -= dmg

    def is_alive(self):
        return self.health > 0
