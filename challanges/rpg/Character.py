class Character:

    def __init__(self, name, health, strength, defence, wisdom, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.wisdom = wisdom
        self.luck = luck
        self.experience = 0
        self.next_level = 10

    def info(self):
        print(self.name,
              self.health,
              self.strength,
              self.defence,
              self.wisdom,
              self.luck)

