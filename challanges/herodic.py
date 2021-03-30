#!/usr/bin/env python3

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }

def getName():
    char_name = input(" Which character do you want to know about? (wolverine, harry Potter, agent fitz)")
    if char_name not in heroes:
        print("Sorry please enter a valid name: Wolverine, Harry Potter, Agent Fitz")
        getName()
    return char_name
def getStat(objName):
    char_state = input("What statistic do you want to know about? (real name, powers, archenemy) ")
    if char_state not in heroes[objName]:
        print("Sorry please enter a valid stat to check out.")
        getStat(objName)
    return char_state

def printMassage(name, stat):
    print(f"{name.title()}'s, {stat} is: {heroes[name][stat]}")
def main():
    res1 = getName()
    res2 = getStat(res1)
    printMassage(res1, res2)

main()
