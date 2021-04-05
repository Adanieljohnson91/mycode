from Area import Area
from enemies import pumpkinMan, kagnor, skeleton, goblin

class Journey:

    def __init__(self, hero):
        self.hero = hero
        self.bed = Area("Bed", ["blanket"], [], "Kagnor raises from the dead and smacks you in the face... you wake up~~~~~~Wait, it was all just a dream~~~~~")
        self.evil_lair = Area("Evil Lair", ["hostage folk", "Sword of Destiny"], [kagnor], f"Ahhh It is i Kagnor, Lord of Darkness, You will fall here today {self.hero.name}...(lover-folk-screams in the background")
        self.dark_forest = Area("Dark Forest", ["torch", "potion", "Flame Storm"], [pumpkinMan, goblin, goblin], "You have done well, {self.name}The dark forest is dark, only in darkness will you gain the thirst to seek the light")
        self.outside = Area("Outside", ["not hostage folk", "necklace of destiny"], [skeleton], "AHHHHH, Kagnor has taken the love of your life, you are now regretting taking you trip outside... note to self, ")
        self.home = Area("Home", ["map"], [], "Its a beautiful day, lets go for a trip... Check out the room see if theres anythin that may help you on your journey")
        self.createJourney()
        self.welcome()
        self.startJourney(self.home)

    def welcome(self):
        print(f"\n\n\nYour story begins, {self.hero.name}, little is known of the adventure that"
              "\nawait. Monsters, Dragons, non-gender-specific love interest "
              "\nsaving, so if you're ready, lets Gooo!!!!")

    def createJourney(self):
        self.bed.addSurrounding(self.home)
        self.home.addSurrounding(self.outside)
        self.outside.addSurrounding(self.dark_forest)
        self.dark_forest.addSurrounding(self.evil_lair)
        self.evil_lair.addSurrounding(self.bed)

    def startJourney(self, area):
        print(area.story)
        while True:
            command = input("What would you like to do?: (SEARCH, FIGHT, VENTURE, GET, QUIT)")
            w1 = command
            if w1.lower() == "search":
                print("ITEMS-->>")
                for item in area.items:
                    print(item)
            if w1.lower() == "venture":
                self.startJourney(area.surrounding[0])
            if w1.lower() == "fight":
                for enemy in area.enemies:
                    while True:
                        hit = self.hero.attack()
                        enemy.takeDamage(hit)
                        if enemy.is_alive():
                            hit = enemy.attack()
                            self.hero.takeDamage(hit)
                        else:
                            print(f"Excellent, you have slain the {enemy.name}")
                            self.hero.add_experience(enemy.health * 10)
                            break
                        if self.hero.is_alive():
                            print("health: ", self.hero.health)
                        else:
                            print("GAME OVER YOU SUCK DOG")
            if w1.lower() == "get":
                for item in area.items:
                    print(item)
                w2 = input("which item are you looking for? ")
                print("ITEMS-->>")

                if w2 in area.items:
                    self.hero.items.append(w2)
                    print("You received a " + w2)



