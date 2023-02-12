# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:40:56 2023

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit

#Clean Up
pl.close("all")

#Load Data
D = np.loadtxt("WGM_SiO2.txt", delimiter = ",", skiprows = 1)
rad = D[:, 0]
P = D[:, 1]

#Plot
pl.figure(1)
pl.plot(rad, P, linestyle = "", marker = ".")
pl.xlabel("Sphere Radius[um]")
pl.ylabel("Power[W]")
pl.title("SiO2")
pl.show()

#Fitting(y = b*exp(ax^2))
x = rad
y = P

def nonlinear_fit(x, a, b):
    return  b * np.exp(a * x**2) #Fittingしたい関数を入れる

popt, cov = curve_fit(nonlinear_fit, x, y)
print('a : {},   b : {}'.format(popt[0], popt[1])) #popt[0]がa,popt[1]がb

pl.figure(2)
x2 = np.linspace(0, 1.65, 1000)
y2 = popt[1] * np.exp(popt[0] * x2**2)
pl.plot(rad, P, linestyle = "", marker = ".", label = "obs") #元データ
pl.plot(x2, y2, label = "model\nPower = bexp(ar^2)") #Fittingした関数のプロット
pl.xlabel("Sphere Radius[um]")
pl.ylabel("Power[W]")
pl.title("SiO2")
pl.legend()
pl.show()