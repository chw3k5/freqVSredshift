__author__ = 'chw3k5'
from matplotlib import pyplot as plt
import numpy, random

colors = ['BlueViolet','Brown','CadetBlue','Chartreuse', 'Chocolate','Coral','CornflowerBlue','Crimson','Cyan',
          'DarkBlue','DarkCyan','DarkGoldenRod', 'DarkGreen','DarkMagenta','DarkOliveGreen','DarkOrange',
          'DarkOrchid','DarkRed','DarkSalmon','DarkSeaGreen','DarkSlateBlue','DodgerBlue','FireBrick','ForestGreen',
          'Fuchsia','Gold','GoldenRod','Green','GreenYellow','HotPink','IndianRed','Indigo','LawnGreen',
          'LightCoral','Lime','LimeGreen','Magenta','Maroon', 'MediumAquaMarine','MediumBlue','MediumOrchid',
          'MediumPurple','MediumSeaGreen','MediumSlateBlue','MediumTurquoise','MediumVioletRed','MidnightBlue',
          'Navy','Olive','OliveDrab','Orange','OrangeRed','Orchid','PaleVioletRed','Peru','Pink','Plum','Purple',
          'Red','RoyalBlue','SaddleBrown','Salmon','SandyBrown','Sienna','SkyBlue','SlateBlue','SlateGrey',
          'SpringGreen','SteelBlue','Teal','Tomato','Turquoise','Violet','Yellow','YellowGreen']
colorLen = len(colors)
random.shuffle(colors)

lineStyles = ['-', ":", "-.", "--"]
lsLen = len(lineStyles)

def readLineTable():
    datafile = "/Users/chw3k5/PycharmProjects/freqVSredShift/linelist.csv"
    with open(datafile) as f:
        lines = f.read().splitlines()

    headers = lines[0].split(":")


    dataDict = {}
    for header in headers:
        dataDict[header] = []

    for singleLine in lines[1:]:
        splitSingleLine = singleLine.split(":")
        for (itemIndex, header) in enumerate(headers):
            dataDict[header].append(splitSingleLine[itemIndex])

    if "Ordered Freq (GHz) (rest frame, redshifted)" in dataDict.keys():
        dataDict["restFreq"] = []
        for freqString in dataDict["Ordered Freq (GHz) (rest frame, redshifted)"]:
            restFreq, redshiftedFreq = freqString.split(',')
            dataDict["restFreq"].append(float(restFreq ))


    lineLists = []
    for (listIndex, chemical) in list(enumerate(dataDict['Chemical Name'])):
        restFreq = dataDict["restFreq"][listIndex]
        quantumNumbers = dataDict["Resolved QNs"][listIndex]
        lineLists.append((restFreq,
                          'GHz',
                          chemical + ' ' + quantumNumbers,
                          colors[listIndex % colorLen],
                          lineStyles[listIndex % lsLen]))


    return lineLists



def getRedshift(obs, rest):
    obs = float(obs)
    rest = float(rest)
    return (rest - obs) / obs


def getC12016():
    name = 'C12016'
    lineList = []
    lineList.append((115.27,'GHz',name+' J:1->0','firebrick','-'))
    return lineList



def makebandplot(minFreq, maxFreq, zMax=10.0, zMin=0.0):
    if zMax < zMin:
        tempVar = zMax
        zMax = zMin
        zMin = tempVar
        del tempVar

    linelist=[]
    # linelist.extend(getC12016())
    linelist.extend(readLineTable())

    lineWidth = 1
    leglines = []
    leglabels = []
    for singleline in linelist:
        (rest, unit, longName, color, ls) = singleline
        rest = float(rest)

        minZ = getRedshift(minFreq, rest)
        maxZ = getRedshift(maxFreq, rest)

        if any([(zMin <= minZ <= zMax), # minZ is inside the bounds
                (zMin <= maxZ <= zMax), # maxZ is inside the bounds
                (maxZ < zMin) and  (zMax < minZ), # maxZ is below lower bound and minZ is above the upper bound, thus the line crosses the plot area
                (minZ < zMin) and (zMax < maxZ) # minZ is below lower bound and maxZ is above the upper bound, thus the line crosses the plot area
                ]):
            plt.plot((minZ, maxZ), (minFreq, maxFreq), color=color, linewidth=lineWidth, ls=ls)
            leglabels.append(longName)
            leglines.append(plt.Line2D(range(10), range(10), color=color, ls=ls, linewidth=lineWidth))


    plt.xlim([zMin, zMax])
    plt.ylim([maxFreq, minFreq])
    plt.xlabel("redshift (z)")
    plt.ylabel("Observed Line Frequency (GHz)")

    plt.legend(leglines, leglabels,
               loc='upper center',
               bbox_to_anchor=(0.5, 1.10),
               numpoints=3,
               handlelength=2,
               prop={'size': 6},
               ncol = 3,
               fancybox = True,
               shadow = True)
    plt.show()
    return



if __name__ == "__main__":
    makebandplot(100.0, 500.0, zMax=3.0, zMin=0.0)
