from random import randint
import csv
'''
Configuration class to be referenced when we are building 
the gemstones
'''
class Configuration:
    unitWidth=14
    unitHeight=16
    viewportWidth=unitWidth
    viewportHeight=unitHeight
    gemstoneWidth=unitWidth
    gemstoneHeight=unitHeight
    gemstoneMultiplier=1
    viewportMultiplier=1
    viewportSize="14x16"
    colors=[]
    stroke=False
    placement="random"
    includeBorders=False
    propensity=100
    backgroundColor="white"
    def setBackgroundColor(self, color):
        self.backgroundColor=color
    def setPropensity(self, propensity):
        self.propensity=propensity
    def setPlacement(self, placement):
        self.placement=placement
    # Create array of selectable color
    def setColors(self, colorString):
        reader = csv.reader(colorString.split('\n'), delimiter=',')
        for row in reader:
            for item in row:
                self.colors.append(item.strip())
        return self.colors
    # Set the viewport multiplier and apply it for reference
    def setViewportMultiplier(self, mult):
        self.viewportMultiplier=mult
        self.viewportHeight=self.unitHeight*mult
        self.viewportWidth=self.unitWidth*mult
        self.viewportSize=str(self.viewportWidth) + "x" + str(self.viewportHeight)
    # Set the gemstone multiplier
    def setGemstoneMultiplier(self, mult):
        self.gemstoneMultiplier=mult
        self.gemstoneWidth=self.unitWidth*mult
        self.gemstoneHeight=self.unitHeight*mult
    def getRandomColor(self):
        index = randint(0, len(self.colors) - 1)
        return self.colors[index]