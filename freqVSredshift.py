__author__ = 'chw3k5'
from matplotlib import pyplot as plt
import numpy
from astropy.table import Table

colors = ['BlueViolet','Brown','CadetBlue','Chartreuse', 'Chocolate','Coral','CornflowerBlue','Crimson','Cyan',
          'DarkBlue','DarkCyan','DarkGoldenRod', 'DarkGreen','DarkMagenta','DarkOliveGreen','DarkOrange',
          'DarkOrchid','DarkRed','DarkSalmon','DarkSeaGreen','DarkSlateBlue','DodgerBlue','FireBrick','ForestGreen',
          'Fuchsia','Gold','GoldenRod','Green','GreenYellow','HotPink','IndianRed','Indigo','LawnGreen',
          'LightCoral','Lime','LimeGreen','Magenta','Maroon', 'MediumAquaMarine','MediumBlue','MediumOrchid',
          'MediumPurple','MediumSeaGreen','MediumSlateBlue','MediumTurquoise','MediumVioletRed','MidnightBlue',
          'Navy','Olive','OliveDrab','Orange','OrangeRed','Orchid','PaleVioletRed','Peru','Pink','Plum','Purple',
          'Red','RoyalBlue','SaddleBrown','Salmon','SandyBrown','Sienna','SkyBlue','SlateBlue','SlateGrey',
          'SpringGreen','SteelBlue','Teal','Tomato','Turquoise','Violet','Yellow','YellowGreen']

def getRedshift(obs,rest,wavelenth=True):
    obs = numpy.array(obs)
    rest = numpy.array(rest)

    if wavelenth:
        return (obs - rest)/rest
    else:
        return (rest - obs)/obs


def getC12016():
    name = 'C12016'
    lineList = []
    lineList.append((115.27,'GHz',name+' J:1->0','firebrick','-'))
    return lineList



def makebandplot(minFreq,maxFreq):
    linelist=[]
    linelist.extend(getC12016())


    for singleline in linelist:
        (rest,unit,longName,color,ls)=singleline
        if unit == 'GHz':
            rest = float(rest)*(10^9)
            doWaveL=False
        else:
            doWaveL=False


        minZ = getRedshift(minFreq,rest,wavelenth=doWaveL)
        maxZ = getRedshift(maxFreq,rest,wavelenth=doWaveL)

        plt.plot(scale_x_vector, scale_y_vector, color=color, linewidth=linw, ls=ls)


    return

if __name__ == "__main__":
    datafile = "/Users/chw3k5/Dissertation/Combined Kappa/code/freqVSredShift/linelist.csv"
    t = Table.read('photometry.dat', format='ascii.daophot')
