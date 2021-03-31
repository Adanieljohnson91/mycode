#!/usr/bin/env python3

from random import randint


def getGuess(correctAnswer, min, max):
    guess = input(f"input a number between {min} and {max}: ")
    if not guess.isdigit():
        print("Invalid entry, please enter a numeric value")
        getGuess(correctAnswer, min, max)
    elif int(guess) < min or int(guess) > max:
        print(f"Try again, guess must be between {min} and {max}")
        getGuess(correctAnswer, min, max)
    elif int(guess) > int(correctAnswer):
        print("Too High")
        getGuess(correctAnswer, min, int(guess))
    elif int(guess) < int(correctAnswer):
        print("Too Low")
        getGuess(correctAnswer, int(guess), max)
    else:
        print("Great Job You are the winner")
        return;


def main():
    value = randint(0, 100)
    getGuess(str(value), 0, 100)


main()
