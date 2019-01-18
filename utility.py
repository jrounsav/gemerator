import os, errno
from gemlocale import validLocations, getCenterNode
from gemstone import buildGemstone
from configuration import Configuration
'''
Just some utility functions
'''

# Build the command line command
def buildCommand(nodes, config, count):
    try:
        os.makedirs("generated")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    baseCommand = 'convert -size ' + config.viewportSize + ' xc:' + config.backgroundColor + ' -fill none '
    for node in nodes:
        gemstoneString=buildGemstone(node, config)
        baseCommand += gemstoneString
    baseCommand += "generated/sticker" + str(count) +".png"
    return baseCommand