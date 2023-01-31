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
Rm1 = np.max(R1)

rad2 = 1.0
D2 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius1.0um.txt", delimiter=",", skiprows=3)
T2 = D2[:, 1]
R2 = -T2
Rm2 = np.max(R2)

rad3 = 1.5
D3 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius1.5um.txt", delimiter=",", skiprows=3)
T3 = D3[:, 1]
R3 = -T3
Rm3 = np.max(R3)

rad4 = 2.0
D4 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius2.0um.txt", delimiter=",", skiprows=3)
T4 = D4[:, 1]
R4 = -T4
Rm4 = np.max(R4)

rad5 = 2.5
D5 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius2.5um.txt", delimiter=",", skiprows=3)
T5 = D5[:, 1]
R5 = -T5
Rm5 = np.max(R5)


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


rad = [rad1, rad2, rad3, rad4, rad5]
Rm = [Rm1, Rm2, Rm3, Rm4, Rm5]


pl.figure(2)
pl.plot(rad, Rm)
pl.xlabel("Core Radius[um]")
pl.ylabel("Rmax")
pl.title("Cylindrical Shell (MoS2)")

#Fitting(y = 1 - b*exp(ax^2))
x = rad
y = Rm

def nonlinear_fit(x, a, b):
    return  1 - b * np.exp(a * x**2)

popt, cov = curve_fit(nonlinear_fit, x, y)

list_y = []
for num in x:
    list_y.append(1 - popt[1] * np.exp(popt[0] * num**2))
    
pl.figure(3)

pl.figure(3)
pl.plot(x, y, label = "obs")
#pl.plot(x, np.array(list_y), label = "fitting")
pl.xlabel("Core Radius[um]")
pl.ylabel("Rmax")
pl.title("Cylindrical Shell (MoS2)")
pl.legend()

print('a : {},   b : {}'.format(popt[0], popt[1]))

#Smoother curve
pl.figure(3)
x2 = np.linspace(0.50, 2.50, 1000)
y2 = 1 - popt[1] * np.exp(popt[0] * x2**2)
pl.plot(x2, y2, label = "model\nRmax = 1 - 0.3exp(-1.3r^2)")
pl.legend()
pl.show()