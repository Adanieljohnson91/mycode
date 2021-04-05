class Area:
    
    def __init__(self, name, items, enemies, story):
        
        self.name = name
        self.items = items
        self.surrounding = []
        self.enemies = enemies
        self.story = story
    
    def getItem(self, name):
        
        res = self.items[name]
        self.items.remove(name)
        return res

    def enemyEncounter(self):

        if self.enemies:
            print("Enemies")
        else:
            print("Safe for now")
    def addSurrounding(self, area):
        self.surrounding.append(area)

    def showSurroundings(self):
        
        for ele in self.surroundings:
            print(ele.name)
    def removeEnemy(self):
        self.enemies
