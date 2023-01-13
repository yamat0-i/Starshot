# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:43:14 2022

@author: User
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up
pl.close("all")

#parameter
#SiO2
c = 3e8 #light speed[m/s]
P = 1e9 #laser power[W]
lam = np.linspace(300e-9,1500e-9,1000) #wavelength[m]
delta = 10e-9 #thickness[m]
rho = 2196 #density[kg/m^3]
#m = rho * ((4/3) * np.pi * (2 * om0)**3 - (4/3) * np.pi * (2 * om0 - delta)**3) #mass of sail[kg]
#om0 = np.sqrt((m * c**2 * lam) / (20 * P * np.pi)) 

#plot
xrange = np.linspace(300e-9, 1500e-9, 150)
yrange = np.linspace(300e-9 , 1500e-9 , 150)
lam, om0 = np.meshgrid(xrange,yrange)

pl.axis([300e-9, 1500e-9, 300e-9, 1500e-9])
pl.gca().set_aspect('equal', adjustable='box')

a = 12 * delta - (15 * P) / (rho * c**2 * lam)
b = -6 * delta**2
c = delta**3
D = b**2 - 4 * a * c
#print(D)
Z = a * om0 **2 + b * om0 + c

pl.contour(lam, om0, Z)
pl.show()