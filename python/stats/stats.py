# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:00:34 2019

@author: klosmarc
"""
from __future__ import division
import math
import numpy as np

def sum_of_squares(x):        
    print([x_i**2 for x_i in x])
    return sum([x_i**2 for x_i in x])
        

def mean(x):
    return sum(x)/len(x)

def de_mean(x):
    x_bar=mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n=len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

def standard_deviation(x):
    return math.sqrt(variance(x))

def covariance(x,y):
    n=len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)


def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x>0 and stdev_y >0:
        return covariance(x,y)/stdev_x/stdev_y
    else:
        return 0
    