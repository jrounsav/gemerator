import csv
'''
Configuration class to be referenced when we are building 
the gemstones
'''
class Configuration:
    colors=[]
    stroke=False
    includeBorders=False
    def setColors(self, colorString):
        reader = csv.reader(colorString.split('\n'), delimiter=',')
        for row in reader:
            for item in row:
                self.colors.append(item.strip())
            return self.colors

