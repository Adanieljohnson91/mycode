from Journey import Journey
class Game:
    def __init__(self, builder):
        self.builder = builder
        Journey(builder.startCharacterJourney())

