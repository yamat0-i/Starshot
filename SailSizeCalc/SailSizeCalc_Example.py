#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 17:46:58 2022

@author: mark
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
Delta = 1e-9 # Thickness of sail in m
lam = 0.5e-6 # Wavelength of illumination
n = 1 # Multiplier of the beam width which gives the radius of the sail
R = n * om0

# Variables
#P = np.linspace(1,1e9,1000) # Power in W
P = 300e9

# Calculate sail mass
m = rho * 4/3 * np.pi * (R**3 - (R-Delta)**3)
if printAll:
    print("Sail mass:")
    print(m)
if printAll:
    print("Sail area:")
    print(4 * np.pi * R**2)

# Calculate Rayleigh length
D = np.pi * om0**2 / lam
if printAll:
    print("Rayleigh length:")
    print(D)

# Calculate and display acceleration
a = 2 * P / (m * c)
if printAll:
    print("Acceleration:")
    print(a)

# Calculate time taken to travel Rayleigh length
t = np.sqrt(2 * D / a)
if printAll:
    print("Time taken to travel Rayleigh length:")
    print(t)

# Velocity change after acceleration
vf = a * t
if printAll:
    print("Velocity change after acceleration (fraction of c):")
    print(vf / c)
    
d = a * t**2 /2
if printAll:
    print("Distance")
    print(d)
    
pl.plot(om0, d, label = "distance")
pl.plot(om0, D, label = "Rayleigh length")
pl.legend()