# Characted Builder class will collect user input via the cmd line
# in order to build a character.
#
from Hero import Hero
from klasses import klasses


class CharacterBuilder:
    STAT_NAMES = ["strength", "wisdom", "luck", "defence", "health"]
    def __init__(self):
        self.name = ""
        self.klass = ""
        self.strength = 0
        self.health = 0
        self.wisdom = 0
        self.luck = 0
        self.defence = 0
        self.property_points = 10

    def startCharacterJourney(self):
        self.enter_name()
        return Hero(self.name,
                    self.health,
                    self.strength,
                    self.defence,
                    self.wisdom,
                    self.luck,
                    self.klass)

    def enter_name(self):
        def getName():
            name = input("E N T E R:> ")
            answer = input(f"Is {name} correct?")
            if answer.lower() == "yes":
                return name
            else:
                return getName()

        print("Good morning sleepy head, its time for an adventure......")
        print("......")
        print("......")
        print("Wait a min, tell me again, What is your name?: ")
        self.name = getName()
        self.select_klass()

    def select_klass(self):
        def print_current(current):
            print(klasses[current]["name"])
            print(klasses[current]["story"])
            print(klasses[current]["strength"])
            print(klasses[current]["wisdom"])
            print(klasses[current]["health"])
            print(klasses[current]["luck"])
        print(f"Great, {self.name}! What is your profession?: ")
        current = 0
        print("Browse by typing \"NEXT\" or \"LAST\"")
        while True:
            print_current(current)
            name = "name"
            print(f"Are you a {klasses[current][name]}")
            selection = input("NEXT, LAST, YES")
            if selection.lower() == "yes":
                print("YES")
                break;
            elif selection.lower() == "next":
                current += 1
            elif selection.lower() == "last":
                current -= 1
        self.klass = klasses[current]
        self.add_klass_props()
        self.add_attributes()

    def add_klass_props(self):
        self.health += self.klass["health"]
        self.strength += self.klass["strength"]
        self.defence += self.klass["defence"]
        self.luck = self.klass["luck"]
        self.wisdom += self.klass["wisdom"]

    def add_attributes(self):
        current = 0
        name = "name"
        print(f"Dang! I knew it, you are a {self.klass[name]}")
        print("Here are your current stats: ")
        self.print_current_stats()
        while self.property_points > 0:
            if current > len(self.STAT_NAMES) - 1 or current < 0:
                current = 0
            response = input(f"Increase {self.STAT_NAMES[current]}? (INC, DEC, NEXT, LAST, VIEW)")
            if response.lower() == "inc":
                self.increaseStatHelper(self.STAT_NAMES[current])
            elif response.lower() == "dec":
                self.decreaseStatHelper(self.STAT_NAMES[current])
                print("Current stats: ", self.print_current_stats())
            elif response.lower() == "next":
                current += 1
            elif response.lower() == "last":
                current -= 1
            elif response.lower() == "view":
                print("Current stats: ", self.print_current_stats())
            else:
                print("Unknown Entry... Stick to the rules")


            

    def print_current_stats(self):
        name = "name"
        print("Class:", self.klass[name], "Strength:", self.strength, "Defence:", self.defence)
        print("Wisdom:", self.wisdom, "Luck:", self.luck)

    def increaseStatHelper(self, stat):
        work = {
            "strength": self.incStrength,
            "defence": self.incDefence,
            "wisdom": self.incWisdom,
            "luck": self.incLuck,
            "health": self.incHealth,
        }
        if stat in work:
            work[stat]()
            self.property_points -= 1
        else:
            print("Invalid entry:")
    def decreaseStatHelper(self, stat):
        work = {
            "strength": self.decStrength,
            "defence": self.decDefence,
            "wisdom": self.decWisdom,
            "luck": self.decLuck,
            "health": self.decHealth,
        }
        if stat in work:
            work[stat]()
        else:
            print("Invalid entry: ")

    def incHealth(self):
        self.health += 1
    def incStrength(self):
        self.strength += 1
    def incLuck(self):
        self.luck += 1
    def incWisdom(self):
        self.wisdom += 1
    def incDefence(self):
        self.defence += 1
    def decHealth(self):
        if self.health < 1:
            print("Error, too low")
        else:
            self.health -= 1
            self.property_points += 1
    def decStrength(self):
        if self.strength < 1:
            print("Error, too low")
        else:
            self.strength -= 1
            self.property_points += 1
    def decLuck(self):
        if self.luck < 1:
            print("Error, too low")
        else:
            self.luck -= 1
            self.property_points += 1
    def decWisdom(self):
        if self.wisdom < 1:
            print("Error, too low")
        else:
            self.wisdom -= 1
            self.property_points += 1
    def decDefence(self):
        if self.defence < 1:
            print("Error, too low")
        else:
            self.defence -= 1
            self.property_points += 1
