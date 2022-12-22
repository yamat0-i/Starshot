# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:27:49 2022

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up plot space
pl.close("all")

D = np.loadtxt('CylindricalShell_5Layer_v3_IntensityCheck.txt', delimiter=",", skiprows=3)
lam = D[:,0]
lam2 = lam * 1e9 #Wavelength [nm]
T = D[:,1]
R = -T #Rreflectance of the sail
print(R)

pl.figure()
pl.plot(lam2, R)
pl.xlabel("Wavelength[nm]", fontsize = 20)
pl.ylabel("Reflectance", fontsize = 20)
pl.title("CylindricalShell_Multilayer(N=5)", fontsize = 25)
pl.tick_params(labelsize = 15)