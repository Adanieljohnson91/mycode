from Character import Character
from random import randint


class Hero(Character):

    def __init__(self, name, health, strength, defence, wisdom, luck, klass):
        super().__init__(name, health, strength, defence, wisdom, luck)
        self.klass = klass
        self.level = 1
        self.items = []
        self.next_level = 10

    def get_health(self):
        return self.health

    def attack(self):
        return self.strength / 10 + randint(0, 10)

    def defend(self):
        return self.defence / 10 + randint(0, 10)

    def add_experience(self, gain):
        self.experience += gain
        if self.experience > self.next_level:
            self.level += 1
            self.next_level += self.level * 5
            print(f"Character leveled up to level {self.level}")
            self.add_experience(0)

    def getItem(self, item):
        self.items.append(item)

    def listItems(self):
        for item in self.items:
            print(item)

    def takeDamage(self, dmg):
        print(f"{self.name} takes {dmg} damage")
        self.health -= dmg
        if self.health > 2 and "potion" in self.items:
            print(f"{self.name} uses a potion, and is healed by 10 health points")
            self.health += 10
            self.items.remove("potion")

    def is_alive(self):
        return self.health > 0

    def p(self):
        print("Name: ", self.name)
        print("Class: ", self.klass["name"])
        print("Health: ", self.health)
        print("Strength: ", self.strength)
        print("Defence: ", self.defence)
        print("Wisdom: ", self.wisdom)
        print("Luck: ", self.luck)

