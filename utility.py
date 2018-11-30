from gemlocale import validLocations, getCenterNode
from gemstone import buildGemstone
from configuration import Configuration
'''
Just some utility functions
'''

# Build the command line command
def buildCommand(nodes, config):
    baseCommand = 'convert -size ' + config.viewportSize + ' xc:' + config.backgroundColor + ' -fill none '
    for node in nodes:
        gemstoneString=buildGemstone(node, config)
        baseCommand += gemstoneString
    baseCommand += "generated.png"
    return baseCommand