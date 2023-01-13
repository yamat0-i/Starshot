# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 19:26:12 2022

@author: 81809
"""

import matplotlib.pyplot as pl
import numpy as np
from matplotlib.pyplot import cm
from mpl_toolkits.mplot3d import Axes3D


rho = 2700 # Density [kg / m^3]
m = 1e-3 #Mass of particle [kg]
#m = 4 / 3 * r**3 * rho*np.pi # Mass of particle
da = 2e-4 #Areal density [kg / m^2]
#r = (m / (8 * np.pi * 1e-4))**(1/2) # Radius of nanoparticle [m]
r = np.linspace(0, 7e-1, 100000)
P0 = 70e9 # Optical power [W]
c = 2.99e8 # Speed of light [m / s]
lam = 1e-6 # Wavelength [m]

#print(r)

om0 = 2 # Beam waist
z = np.linspace(0,1e5,100000) #z[m]
zR = np.pi * om0**2 / lam # Rayleigh length[m]
om = om0 * np.sqrt(1 + (z / zR)**2) # Beam waist at position z
I0 = P0 / (np.pi * om0**2) # Intensity at beam waist
#I = I0 * (om0 / om)**2 * np.exp(-2 * r**2 / (om**2)) # Intensity at particle radius
P = P0 * (1 - np.exp(-r**2 / om**2)) # Approximate power of beam within particle radius

#pl.figure(5)
fig,ax = pl.subplots(projection='3d')
ax.plot(r, z, P, linewidth = 0, cmap = cm.coolwarm)