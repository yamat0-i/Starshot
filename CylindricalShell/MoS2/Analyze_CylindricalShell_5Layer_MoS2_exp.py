# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:25:55 2023

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit

pl.close("all")

rad1 = 0.5  #Core radius[um]
D1 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius0.5um.txt", delimiter=",", skiprows=3)
lam = D1[:,0] * 1e9 #wavelength[nm]
T1 = D1[:, 1]
R1 = -T1

rad2 = 1.0
D2 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius1.0um.txt", delimiter=",", skiprows=3)
T2 = D2[:, 1]
R2 = -T2

rad3 = 1.5
D3 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius1.5um.txt", delimiter=",", skiprows=3)
T3 = D3[:, 1]
R3 = -T3

rad4 = 2.0
D4 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius2.0um.txt", delimiter=",", skiprows=3)
T4 = D4[:, 1]
R4 = -T4

rad5 = 2.5
D5 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius2.5um.txt", delimiter=",", skiprows=3)
T5 = D5[:, 1]
R5 = -T5

pl.figure(1)
pl.plot(lam, R1, label = "o.5um")
pl.plot(lam, R2, label = "1.0um")
pl.plot(lam, R3, label = "1.5um")
pl.plot(lam, R4, label = "2.0um")
pl.plot(lam, R5, label = "2.5um")
pl.xlabel("wavelength[nm]")
pl.ylabel("R")
pl.title("Cylindrical Shell (MoS2)")
pl.legend()

#Rm(1.2um)
rad = [rad1, rad2, rad3, rad4, rad5]

Rm1 = -D1[6, 1]
Rm2 = -D2[6, 1]
Rm3 = -D3[6, 1]
Rm4 = -D4[6, 1]
Rm5 = -D5[6, 1]

Rm = [Rm1, Rm2, Rm3, Rm4, Rm5]

pl.figure(2)
pl.plot(rad, Rm)
pl.xlabel("Core Radius[um]")
pl.ylabel("Rmax(λ=1.2um)")
pl.title("Cylindrical Shell (MoS2)")

#Fitting(y = 1 - b*exp(ax^2))
x = rad
y = Rm

def nonlinear_fit(x, a, b):
    return  0.92 - b * np.exp(a * x**2)

popt, cov = curve_fit(nonlinear_fit, x, y)

list_y = []
for num in x:
    list_y.append(0.92 - popt[1] * np.exp(popt[0] * num**2))

print('a : {},   b : {}'.format(popt[0], popt[1]))

pl.figure(3)
pl.figure(3)
pl.plot(x, y, label = "obs", linestyle = "", marker = ".")
#pl.plot(x, np.array(list_y), label = "fitting")
x2 = np.linspace(0.50, 2.50, 1000)
y2 = 0.92 - popt[1] * np.exp(popt[0] * x2**2)
pl.plot(x2, y2, label = "model\ny = 0.92 - 0.29exp(-0.79x^2)")
pl.legend()
pl.xlabel("Core Radius[um]")
pl.ylabel("Rmax(λ=1.2um)")
pl.title("Cylindrical Shell (MoS2)")
pl.show()