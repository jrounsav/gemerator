#!/usr/bin/python
import subprocess, sys, getopt, time, shlex
from gemlocale import validLocations
# commands = [ "echo worksssssss" ]
# programs = [subprocess.Popen(c.split()) for c in commands]

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

viewportMultiplier= input("Please enter a viewport multiplier: ")
gemstoneMultiplier= input("Please enter a gemstone size multiplier less than or equal to the viewport: ")

viewportWidth=14*viewportMultiplier
viewportHeight=16*viewportMultiplier
viewportSize = str(viewportWidth) + "x" + str(viewportHeight)

print("Viewport size of: " + viewportSize)

# Baseline command to initiate the draw space
convert = "convert -size " + viewportSize + " xc:white -fill none"
validLocations(viewportMultiplier, gemstoneMultiplier)




# programs = [subprocess.Popen(shlex.split(commands))]