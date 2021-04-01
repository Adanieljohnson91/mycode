#!/usr/bin/env python3
import json

story = json.load(open("story.json"))


def playStory(_story=story):
    def selectNumber(options, current):
        try:
            selection = input(_story[current]["answers"])
            selection = int(selection)
        except:
            print("Invalid Selection")
            return selectNumber(options, current)

        if selection > 0 and selection < len(options):
            return _story[current]["routes"][selection - 1]
        else:
            print(f"Sorry your Selection must be between 1 and {len(options)}")
            return selectNumber(options, current)

    def readPrompt(current):
        question = _story[current]["question"]
        print(question)

    def playStoryHelper(current=0):
        readPrompt(current)
        options = _story[current]["routes"]
        if options:
            current = selectNumber(options, current)
            playStoryHelper(current)
        else:
            print("Finished, do come back if you have a problem")

    playStoryHelper()


def main():
    playStory()


main()
