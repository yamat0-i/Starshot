# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:59:07 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up plot environment
pl.close("all")

# Constants
rho = 2.65 / 1000 * 100**3 # Density of silica in kg / m^3
c = 2.99e8 # Speed of light

# Parameters
Delta = 10e-9 # Thickness of sail in m
lam = 1.5e-6 # Wavelength of illumination
s = 1 # Multiplier of the beam width which gives the radius of the sail

vt = 0.1 * c

# Variables
P = np.linspace(4.5e11,2000e9,1000) # Power in W
# Quadratic equation coefficients
A = 1 - P / (s**2 * vt**2 * rho * Delta * c * lam)
print("A")
print(A)

B = -Delta
print("B")
print(B)
            
C = 1/3 * Delta**2
print("C")
print(C)

# Calculate B^2 - 4 * A * C

check = B**2 - 4 * A * C

# Plot
pl.figure(1)
pl.plot(P, check)
pl.grid("on")

rsp = -(B + np.sqrt(B**2-4 * A * C)) / (2 * A)
rsm = -(B - np.sqrt(B**2-4 * A * C)) / (2 * A)

pl.figure(2)
pl.plot(P, rsp, 'r-', label = "rs+")
pl.plot(P, rsm, 'b-', label = "rs-")
pl.legend()
pl.show()