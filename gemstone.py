'''
This file contains all abstracted functions necessary to generate 
pieces of the gemstones.
'''
def buildGemstone(center, gemMult, config):
    print("Should build gemstone")
    
    # Generate Top of Gemstone
    topLeftString=buildTopLeft(center, gemMult)
    topString=buildTop(center, gemMult)
    topRightString=buildTopRight(center, gemMult)
    topSection=topLeftString + topString + topRightString

    # Generate middle of Gemstone
    left=buildLeft(center, gemMult)
    middleLeft=buildLeftMiddle(center, gemMult)
    middle=buildMiddle(center, gemMult)
    middleRight=buildRightMiddle(center, gemMult)
    right=buildRight(center, gemMult)
    middleSection=left+middleLeft+middle+middleRight+right

    # Generate bottom of Gemstone
    bottomLeft=buildBottomLeft(center, gemMult)
    bottomRight=buildBottomRight(center, gemMult)
    bottomSection=bottomLeft+bottomRight

    wholeString = topSection + middleSection + bottomSection
    return wholeString

def buildTopLeft(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]-(7*multiplier)
    pointOneY=center[1]-(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]-(4*multiplier)
    pointTwoY=center[1]-(3*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]-(8*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildTop(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]-(4*multiplier)
    pointOneY=center[1]-(3*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]
    pointTwoY=center[1]-(8*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]+(4*multiplier)
    pointThreeY=center[1]-(3*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildTopRight(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]+(7*multiplier)
    pointOneY=center[1]-(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]+(4*multiplier)
    pointTwoY=center[1]-(3*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]-(8*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildLeft(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]-(7*multiplier)
    pointOneY=center[1]-(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]-(4*multiplier)
    pointTwoY=center[1]-(3*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]-(7*multiplier)
    pointThreeY=center[1]+(4*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildLeftMiddle(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]-(7*multiplier)
    pointOneY=center[1]+(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]-(4*multiplier)
    pointTwoY=center[1]-(3*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]+(5*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildMiddle(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]-(4*multiplier)
    pointOneY=center[1]-(3*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]+(4*multiplier)
    pointTwoY=center[1]-(3*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]+(5*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildRightMiddle(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]+(4*multiplier)
    pointOneY=center[1]-(3*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]+(7*multiplier)
    pointTwoY=center[1]+(4*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]+(5*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildRight(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]+(7*multiplier)
    pointOneY=center[1]-(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]+(4*multiplier)
    pointTwoY=center[1]-(3*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]+(7*multiplier)
    pointThreeY=center[1]+(4*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildBottomLeft(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]-(7*multiplier)
    pointOneY=center[1]+(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]
    pointTwoY=center[1]+(5*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]+(8*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

def buildBottomRight(center, multiplier):
    # Get coordinates of first corner
    pointOneX=center[0]+(7*multiplier)
    pointOneY=center[1]+(4*multiplier)
    coordOne=str(int(pointOneX)) + "," + str(int(pointOneY))

    # Get second corner coordinates
    pointTwoX=center[0]
    pointTwoY=center[1]+(5*multiplier)
    coordTwo=str(int(pointTwoX)) + "," + str(int(pointTwoY))

    # Get third corner coordinates
    pointThreeX=center[0]
    pointThreeY=center[1]+(8*multiplier)
    coordThree=str(int(pointThreeX)) + "," + str(int(pointThreeY))

    # Put ImageMagick string together
    coordinates=[coordOne, coordTwo, coordThree]
    drawString = makeString(coordinates)
    return drawString

'''
Given an array of string coordinates, greate the string to be used
by the ImageMagick function.
'''
def makeString(points):
    # Example with stroke
    # TODO: Add a configuration option that will allow stroke to be set
    # TODO: Use the colors set by the configuration
    drawString='-draw "fill #8C1D40 stroke #FFC23F stroke-width 3 polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    # drawString=' -draw "fill #8C1D40 stroke none polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    return drawString