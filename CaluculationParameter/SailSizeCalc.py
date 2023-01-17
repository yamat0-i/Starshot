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

# Constants
rho = 2.65 / 1000 * 100**3 # Density of silica in kg / m^3
c = 2.99e8 # Speed of light

# Parameters
Delta = 1e-5 # Thickness of sail in m
lam = 1.5e-6 # Wavelength of illumination
n = 2 # Multiplier of the beam width which gives the radius of the sail

# Variables
P = np.linspace(1,1e9,1000) # Power in W

# Quadratic equation coefficients
A = n**2 * Delta * rho - 100 * P / (lam * c**3)

B = -n * Delta**2 * rho

C = Delta**3 * rho / 3

# Calculate B^2 - 4 * A * C

check = B**2 - 4 * A * C

# Plot
pl.plot(P, check)




