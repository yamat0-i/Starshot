# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:55:15 2022

@author: 81809
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
delta = 1200e-9 #thickness[m]
rho = 2196 #density[kg/m^3]
#m = rho * ((4/3) * np.pi * (2 * om0)**3 - (4/3) * np.pi * (2 * om0 - delta)**3) #mass of sail[kg]
#om0 = np.sqrt((m * c**2 * lam) / (20 * P * np.pi)) 


a = 12 * delta
b = -6 * delta**2
c = delta**3 - 1200 * P * lam / ((np.pi)**2 * c**3)
print("a")
print(a)
print("b")
print(b)
print("c")
print(c)
D = b**2 - 4 * a * c
print(D)
"""
p = (rho * lam * c**3 / 300) * (12 * delta + (b**2 / 4 * c))
print("p")
print(p)
pl.figure(1)
pl.plot(lam, p)
pl.xlabel("λ[m]")
pl.ylabel("Power[W]")


om0 = (-b + np.sqrt(D)) / 2 * a
print("om0")
print(om0)
pl.figure(2)
pl.plot(lam,om0)
pl.xlabel("λ[m]")
pl.ylabel("ω0[m]")
"""
