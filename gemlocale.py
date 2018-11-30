import random
'''
Gem Locale
These helper functions find all of the nodes from which we can generate gemstone polygons inside of a viewport.

This logic currently assumes that we are building out from the center.
'''

'''
Return the center points of all possible gemstones in a viewport.
Note that this includes gems on the border.
'''
def validLocations(config):
    viewWidth=config.viewportWidth
    viewHeight=config.viewportHeight

    view=[viewWidth, viewHeight]
    center = getCenterNode(viewWidth, viewHeight)

    nodes = getNodeCoords(center, view, config)
    nodes = applyPlacement(nodes, config)
    return nodes

def applyPlacement(nodes, config):
    placement = config.placement
    if placement == "random":
        nodes=randomPropensity(nodes, config)
    elif placement == "circulars":
        print("Circulars applied")
    elif placement == "triad":
        print("Triad applied")
    return nodes

def randomPropensity(nodes, config):
    propensity=config.propensity/100
    print("Propensity is " + str(propensity))
    nodes=random.sample(nodes,int(len(nodes)*(propensity)))
    return nodes

'''
Returns the dead center of the viewport. all gems are built off of this point
'''
def getCenterNode(width, height):
    return[width/2, height/2]

'''
Get the coordinates of all non-center nodes.
A node is the center of a gemstone polygon to be built out
'''
def getNodeCoords(center, view, config):
    gemWidth = config.gemstoneWidth
    gemHeight = config.gemstoneHeight
    gemMult = config.gemstoneMultiplier
    validNodes = []

    startY = center[1]
    startX = center[0]
    shiftXValue = 0.5*gemWidth
    shiftYValue = gemHeight-(4*gemMult)
    shift=False
    # Get valid centers AT and ABOVE the center
    while startY >= 0:
        if shift == True:
            startX -= shiftXValue
        else:
            startX = center[0]
        inlineVals = inlineXvals(startX, view[0], gemWidth)
        for val in inlineVals:
            validNodes.append([int(val), int(startY)])

        shift = not shift
        startY -= shiftYValue

    startX = center[0]
    shift=True
    startY = center[1]+shiftYValue
    # Get valid centers below the center
    while startY <= view[1]:
        if shift == True:
            startX -= shiftXValue
        else:
            startX = center[0]
        inlineVals = inlineXvals(startX, view[0], gemWidth)
        for val in inlineVals:
            validNodes.append([int(val), int(startY)])

        shift = not shift
        startY += shiftYValue
    return validNodes

'''
Given a start, get all nodes to the left and right of the start point.
'''
def inlineXvals(mainX, viewEnd, gemWidth):
    x = mainX
    validX = []
    while x >= 0:
        if x >= 0:
            validX.append(x)
        x -= gemWidth
    x = mainX + gemWidth # We shift mainX to the right to avoid duplicating center
    while x <= viewEnd:
        if x<= viewEnd:
            validX.append(x)
        x += gemWidth
    return validX

