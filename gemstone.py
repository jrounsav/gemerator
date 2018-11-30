'''
This file contains all abstracted functions necessary to generate 
pieces of the gemstones.
'''
def buildGemstone(center, config):
    
    # Generate Top of Gemstone
    topLeftString=buildTopLeft(center, config)
    topString=buildTop(center, config)
    topRightString=buildTopRight(center, config)
    topSection=topLeftString + topString + topRightString

    # Generate middle of Gemstone
    left=buildLeft(center, config)
    middleLeft=buildLeftMiddle(center, config)
    middle=buildMiddle(center, config)
    middleRight=buildRightMiddle(center, config)
    right=buildRight(center, config)
    middleSection=left+middleLeft+middle+middleRight+right

    # Generate bottom of Gemstone
    bottomLeft=buildBottomLeft(center, config)
    bottomRight=buildBottomRight(center, config)
    bottomSection=bottomLeft+bottomRight

    wholeString = topSection + middleSection + bottomSection
    return wholeString

def buildTopLeft(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildTop(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildTopRight(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildLeft(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildLeftMiddle(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildMiddle(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildRightMiddle(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildRight(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildBottomLeft(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

def buildBottomRight(center, config):
    multiplier=config.gemstoneMultiplier
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
    drawString = makeString(coordinates, config)
    return drawString

'''
Given an array of string coordinates, greate the string to be used
by the ImageMagick function.
'''
def makeString(points, config):
    color1=config.getRandomColor()
    color2="#FFC23F"
    drawString='-draw "fill ' + color1 + ' polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    # drawString='-draw "fill ' + color1 + ' stroke ' + color2 + ' stroke-width 3 polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    # drawString='-draw "fill ' + color + ' stroke #FFC23F stroke-width 3 polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    # drawString='-draw "fill ' + color + ' stroke #FFC23F stroke-width 3 polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    # drawString=' -draw "fill #8C1D40 stroke none polygon ' + points[0] + ' ' + points[1] + ' ' + points[2] + '" '
    return drawString