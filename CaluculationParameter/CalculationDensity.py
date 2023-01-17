# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:27:41 2023

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up plot environment
pl.close("all")

# Switches
printAll = True

A = 10 #illuminated Area[m^2]
r = np.abs(A / np.pi**2) #Radius of Illuminated Area[m^2]

n = 1
R = r * n #Radius of sail[m]
print("Radius of sail")
print(R)

m = 1e-3 #Mass of Sail[kg]

delta1 = np.linspace(30e-9, 100e-9, 1000)
rho1 = m / (A * delta1)
print("Density(Planar Sail)")
print(rho1)
pl.figure(1)
pl.plot(delta1, rho1)
pl.title("Density(Planar Sail)")

rho2 = 3 * m / (4 * R**3 * np.pi)
print("Density(Sphere)")
print(rho2)

delta3 = np.linspace(30e-9, 100e-9, 1000)
rho3 = 3 * m / (4 * np.pi * (R**3 - (R - delta3)**3))
print("Density(Shell)")
print(rho3)
pl.figure(3)
pl.plot(delta3, rho3)
pl.title("Density(Shell)")
