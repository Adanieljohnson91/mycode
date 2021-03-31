from random import randint


def getGuess(correctAnswer, min, max):
    guess = input(f"input a number between {min} and {max}: ")
    if guess.isdigit() == False:
        print("Invalid entry, please enter a numeric value")
        getGuess(correctAnswer, min, max)
    if int(guess) < min or int(guess) > max:
        print(f"Try again, guess must be between {min} and {max}")
        getGuess(correctAnswer, min, max)
    if int(guess) > int(correctAnswer):
        print("Too High")
        getGuess(correctAnswer, min, int(guess))
    if int(guess) <  int(correctAnswer):
        print("Too Low")
        getGuess(correctAnswer, int(guess), max)
    else:
        print("Great Job You are the winner")

def main():
    value = randint(0, 100)
    getGuess(str(value), 0, 100)

main()
