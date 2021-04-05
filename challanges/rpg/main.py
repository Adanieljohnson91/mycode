from Game import Game
from CharacterBuilder import CharacterBuilder
def main():
    game = Game(CharacterBuilder())
    game.start()


if __name__ == '__main__':
    main()

