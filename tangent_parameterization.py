# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:48:14 2022

@author: Robert
"""

import scipy.integrate as integrate
import math
import numpy as np
import matplotlib.pyplot as plt
import time


def calcXAnalytic(theta, pairs):
    a_sum = 0
    b_sum = 0
    for k in range(2, len(pairs), 1):
        a,b = pairs[k].split(',')
        a = float(a)
        b = float(b)
        a_sum += (a/2) * (((1 - (np.cos((k+1)*theta))) / (k + 1)) + ((1 - (np.cos((k - 1)*theta))) / (k - 1)))
        b_sum += (b/2) * (((np.sin((k+1)*theta)) / (k + 1)) + ((np.sin((k - 1)*theta)) / (k - 1)))

    a,b = pairs[0].split(',')
    b = float(b)
    return a_sum + b_sum + (b * np.sin(theta))

def calcYAnalytic(theta, pairs):
    a_sum = 0
    b_sum = 0
    for k in range(2, len(pairs), 1):
        a,b = pairs[k].split(',')
        a = float(a)
        b = float(b)
        a_sum += (a/2) * (-(((np.sin((k+1)*theta))) / (k + 1)) + (((np.sin((k - 1)*theta))) / (k - 1)))
        b_sum += (b/2) * (((1 - (np.cos((k+1)*theta))) / (k + 1)) + (((np.cos((k - 1)*theta)) - 1) / (k - 1)))

    a,b = pairs[0].split(',')
    b = float(b)
    return a_sum + b_sum + (b * (1 - np.cos(theta)))

def plotPoints(fname):

    x_list = []
    y_list = []
    pairs = []

    with open(fname) as fp:
        for line in fp:
            line = line.strip()
            pairs = line.split('~')

    ep = math.pi/100

    #adding epsilon will add 1 last point which ends up near the beginning point of graph
    for theta in np.arange(0,(2*math.pi)+ep,ep):
        x = calcXAnalytic(theta, fname, pairs)
        y = calcYAnalytic(theta, fname, pairs)
        x_list += [x]
        y_list += [y]

    print(len(x_list))
    print(f'x list: {x_list}')
    print(f'y list: {y_list}')

    plt.axes().set_aspect('equal')
    #plt.scatter(x_list,y_list)
    plt.plot(x_list,y_list)

def getPoints(pairs, theta_list):

    x_list = []
    y_list = []

    for theta in theta_list:
        x = calcXAnalytic(theta, pairs)
        y = calcYAnalytic(theta, pairs)
        x_list += [x]
        y_list += [y]

    return(x_list, y_list)


if __name__ == '__main__':
    fname_list = 'coeff1.txt'
    plotPoints(fname_list)