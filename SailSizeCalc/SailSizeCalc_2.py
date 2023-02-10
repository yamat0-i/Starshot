# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:00:58 2023

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up plot environment
pl.close("all")

# Switches
printAll = True

# Constants
rho = 2320 # Density of silica in kg / m^3
c = 2.99e8 # Speed of light

# Parameters
#om0 = 0.5 
om0 = np.linspace(0.01,0.1,1000) # Beam radius in m
Delta = 1200e-9 # Thickness of sail in m
lam = 0.5e-6 # Wavelength of illumination
n = 1 # Multiplier of the beam width which gives the radius of the sail
R = n * om0

# Variables
I = 10e9 #Laser Intencity[W/m^2]
P = I * np.pi * om0**2 # Laser Power[W]

# Calculate sail mass
m = rho * 4/3 * np.pi * (R**3 - (R-Delta)**3)
if printAll:
    print("Sail mass:")
    print(m)
if printAll:
    print("Sail area:")
    print(4 * np.pi * R**2)
    
#Time
t = np.linspace(100, 10000, 1000)

#Velocuty Gain
v = 2 * P * t / (m * c)
if printAll:
    print("Velocity Gain")
    print(v)

#Distance to Travel
d = P * t**2 / (m * c)
if printAll:
    print("Distance to Travel")
    print(d)
    
pl.plot(t, v, label = "v")
pl.plot(t, d, label = "d")
pl.legend()