#!/usr/bin/python
import subprocess, sys, getopt, time, shlex, json
from pprint import pprint
from gemlocale import validLocations, getCenterNode
from gemstone import buildGemstone
from configuration import Configuration
from utility import buildCommand
'''
Python script that generates an ImageMagick convert command.

TODO:   
        - Handle gemstone circulars
        - Handle gemstone triad
        - Handle custom asset placement
        - Handle custom Coordinate selection
'''

##### Get to this
# convert -size 14x16 xc:none -fill none \
#           -draw "fill #8C1D40 stroke none polygon 30,50 110,50 70,130" \
#           -draw "fill #8C1D40 stroke none polygon 30,50 110,50 70,130" \
#           ~/generated.gif
#####

# Clear terminal
print(chr(27) + "[2J")

unitWidth=14
unitHeight=16
config = Configuration()

welcome="Welcome to the AR Sticker Generator! \n"
description="""This program attempts to generate a random number of semi-randomly
colored gemstone polygons to be used in AR Image Recognition. You may defined the scale
of both the gems as well as the propensity for them to render inside of their viewport.
Once rendered, they should be output to a local folder inside of your executing directory.

Please note that the base size of a gem(in pixels) is 14x16, and the scales must reflect 
some multiple of that.
"""

def noConfigProvided():
    print(welcome)
    print(description)

    ## Get user input Here
    viewportMultiplierRaw= input("Please enter a viewport multiplier: ")
    viewportMultiplier=int(viewportMultiplierRaw)
    gemstoneMultiplierRaw= input("Please enter a gemstone size multiplier less than or equal to the viewport: ")
    gemstoneMultiplier=int(gemstoneMultiplierRaw)
    colors= input("Please enter a csv of HEX colors that you would like to use on the stickers: ")
    placement= input("Please define how you would like the gemstones to be placed: ")
    propensity= input("What percentage of the viewport would you like populated: ")

    # Start building the configuration object
    colors = config.setColors(colors)
    config.setViewportMultiplier(viewportMultiplier)
    config.setGemstoneMultiplier(gemstoneMultiplier)
    config.setPlacement(placement)
    config.setPropensity(propensity)

def configProvided(file):
    # Open and utilize file
    print("Configuration coming from: " + file)
    with open(file) as f:
        data = json.load(f)
    config.setColors(data["colors"])
    config.setViewportMultiplier(data["viewportMultiplier"])
    config.setGemstoneMultiplier(data["gemstoneMultiplier"])
    config.setPlacement(data["placement"])
    config.setPropensity(data["propensity"])
    config.setBackgroundColor(data["backgroundColor"])
    config.setNumberOfGems(data["numberOf"])

# If a config file is provided then we attempt to use it
def invokeBranch(argv):
    if len(argv) > 0:
        configProvided(argv[0])
    else:
        noConfigProvided()

invokeBranch(sys.argv[1:])

for x in range(config.numberOf):
    # Get all valid locations for building gems
    nodes = validLocations(config)

    # Generate the ImageMagick command that is to be passed back to the shell
    commands = buildCommand(nodes, config, x)

    programs = [subprocess.Popen(shlex.split(commands))]