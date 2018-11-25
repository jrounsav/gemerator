#!/usr/bin/python
import subprocess, sys, getopt, time, shlex
from gemlocale import validLocations, getCenterNode
from gemstone import buildGemstone
from configuration import Configuration
'''
Python script that generates an ImageMagick convert command.

TODO:   - Randomly place and generate gemstones on nodes
        - Apply configuration colors
        - Enable color randomization
        - Determine future of strokes, given that they can get pointy
        - Build secondary command line interface that accepts arguments
            only. Rather than prompt a user for config input.
        - Generate proper names for generated files.
        - Accept a count for the number of views desired
        - Accept counts for gemstone proclivity
'''

# def main(argv):
#     for arg in argv:
#         print arg

# main(sys.argv[1:])

##### Get to this
# convert -size $sizex"x"$sizey xc:none -fill none \
#           -draw "fill #8C1D40 stroke none polygon 30,50 110,50 70,130" \
#           -draw "fill #8C1D40 stroke none polygon 30,50 110,50 70,130" \
#           ~/generated.gif
#####

# Clear terminal
print(chr(27) + "[2J")

unitWidth=14
unitHeight=16

welcome="Welcome to the AR Sticker Generator! \n"
description="""This program attempts to generate a random number of semi-randomly
colored gemstone polygons to be used in AR Image Recognition. You may defined the scale
of both the gems as well as the propensity for them to render inside of their viewport.
Once rendered, they should be output to a local folder inside of your executing directory.

Please note that the base size of a gem(in pixels) is 14x16, and the scales must reflect 
some multiple of that.
"""

print(welcome)
print(description)

## Get user input Here
viewportMultiplierRaw= input("Please enter a viewport multiplier: ")
viewportMultiplier=int(viewportMultiplierRaw)
gemstoneMultiplierRaw= input("Please enter a gemstone size multiplier less than or equal to the viewport: ")
gemstoneMultiplier=int(gemstoneMultiplierRaw)
colors= input("Please enter a csv of HEX colors that you would like to use on the stickers: ")

viewportWidth=14*viewportMultiplier
viewportHeight=16*viewportMultiplier
viewportSize = str(viewportWidth) + "x" + str(viewportHeight)
print("Viewport size of: " + viewportSize)

# Get all valid locations for building gems
nodes = validLocations(viewportMultiplier, gemstoneMultiplier)
print("All nodes" + str(nodes))

# Start building the configuration object
config = Configuration()
colors = config.setColors(colors)
print("All provided colors" + str(colors))

# Build a gemstone
# NOTE: This is a test. We need to use the valid locations and be random about the generation.
baseCommand = 'convert -size ' + viewportSize + ' xc:white -fill none '

center=getCenterNode(viewportWidth, viewportHeight)
gemstoneString=buildGemstone(center, gemstoneMultiplier, config)
baseCommand += gemstoneString
baseCommand += "generated.png"
print(baseCommand)
commands = baseCommand
programs = [subprocess.Popen(shlex.split(commands))]