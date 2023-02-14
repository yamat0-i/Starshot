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
SA=10 # Sail area
om0 = 4 * np.sqrt(SA/(4 * np.pi)) # Set beam radius to sail radius according to sail area
Delta = 10e-9 # Thickness of sail in m
lam = 0.5e-6 # Wavelength of illumination
s = 1 # Multiplier of the beam width which gives the radius of the sail
sr = np.linspace(10e-9,100e-9,100)
om0 = s * sr

if printAll:
    print("Beam waist size (m)")
    print(om0)
    
# Variables
#P = np.linspace(1,1e9,1000) # Power in W
P = 1000e9

# Calculate sail mass
m = rho * 4/3 * np.pi * (sr**3 - (sr-Delta)**3)
if printAll:
    print("Sail mass:")
    print(m)
if printAll:
    print("Sail area:")
    print(4 * np.pi * sr**2)

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
vf = np.sqrt(2) * a * t # After the beam starts to expand, the final speed is sqrt(2) times the speed at the Rayleigh distance
if printAll:
    print("Velocity change after acceleration (fraction of c):")
    print(vf / c)
    
    
pl.figure(1)
pl.plot(2 * sr * 1e9, vf / c, '.-')
pl.xlabel("Sail diameter (nm)")
pl.ylabel("vf / c")