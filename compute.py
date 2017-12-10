from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob



# def damped_vibrations(t, A, b, w):
#     return A*exp(-b*t)*cos(w*t)
#
# def compute(A, b, w, T, resolution=500):
#     """Return filename of plot of the damped_vibration function."""
#     t = linspace(0, T, resolution+1)
#     u = damped_vibrations(t, A, b, w)
#     plt.figure()  # needed to avoid adding curves in plot
#     plt.plot(t, u)
#     plt.title('A=%g, b=%g, w=%g' % (A, b, w))
#     if not os.path.isdir('static'):
#         os.mkdir('static')
#     else:
#         # Remove old plot files
#         for filename in glob.glob(os.path.join('static', '*.png')):
#             os.remove(filename)
#     # Use time since Jan 1, 1970 in filename in order make
#     # a unique filename that the browser has not chached
#     plotfile = os.path.join('static', str(time.time()) + '.png')
#     plt.savefig(plotfile)
#     return plotfile
#
# if __name__ == '__main__':
#     print (compute(1, 0.1, 1, 20))






import math
import matplotlib.pyplot as plt
from fractions import Fraction
import pandas as pd
import numpy as np
import os, time, glob

def showTabel(tabel):
    df = pd.DataFrame(tabel, ['sinFi', 'y', 't'], ['0', 'pi/2', 'pi', '3pi/2', '2pi'])
    print(df)

def initTabel(coloane,linii):
    tabel = [[0 for x in range(coloane)] for y in range(linii)]
    return tabel


def valueTabel(tabel,sinFi,lege,t):
    tabel[0]=sinFi
    tabel[1]=lege
    tabel[2]=t

def y(A,w,t,fi0):
    elongatia= A*math.sin(w*t+fi0)
    fi=w*t+fi0

def v(A,w,t,fi0):
    viteza= A*w*math.cos(w*t+fi0)
    fi=w*t+fi0

def a(w,A,t,fi0):
    acceleratia= -(w**2)*A*math.sin(w*t+fi0)
    fi=w*t+fi0

fi=[0,90,180,270,360]
cosfi=[1,0,-1,0,1]
sinfi=[0,1,0,-1,0]

#Input
# A=int(input('A= '))
# fi0=int(input('fi0= '))
# w=int(input('w= '))

#Precucare
# t=(fi-fi0)/w
# fifinal=fi-fi0

# string=str(Fraction(fifinal,w))
# string=string.split('/')
# a=string[0]
# b=string[1]
#print(a+'/'+b)


def compute(A,w,fi0):

    fi=[0,90,180,270,360]
    cosfi=[1,0,-1,0,1]
    sinfi=[0,1,0,-1,0]

    lege=[]
    t=[]
    intt=[]

    for i in range(5):
        lege.append(A*sinfi[i])
        t.append(str(Fraction(fi[i]-fi0,w)))
        intt.append(int(t[i].split('/')[0]))

    # tabel=initTabel(5,3)
    # valueTabel(tabel,sinfi,lege,t)
    # showTabel(tabel)


    x=intt
    y=lege

    # calculate polynomial
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)    # tabel=initTabel(5,3)

    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 100)
    y_new = f(x_new)

    plt.plot(x,y,'o', x_new, y_new)
    # plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.axhline(y=0, xmin=x[0], xmax=x[4], hold=None,color='black')
    plt.axvline(x=0,ymin=-100,ymax=100,hold=None,color='black')

    plt.axhline(y=y[1], xmin=x[0], xmax=x[4], hold=None,linestyle='dashed',color='red')
    plt.axhline(y=y[3], xmin=x[0], xmax=x[4], hold=None,linestyle='dashed',color='red')



    plt.vlines(1,0,25,color='blue',linestyle='dotted')
    plt.vlines(5,0,-25,color='blue',linestyle='dotted')

    plt.xlabel('t(m)*'+str(t[1]))
    plt.ylabel('y(m)')


    plt.text(-1,y[1]+1,y[1])
    plt.text(-1,y[3]+1,y[3])

    # plt.figure()  # needed to avoid adding curves in plot
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)
    plt.close()
    return plotfile
