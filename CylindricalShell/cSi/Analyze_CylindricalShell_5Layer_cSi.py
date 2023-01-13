# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:34:27 2022

@author: markt
"""

import numpy as np
import matplotlib.pyplot as pl

pl.close("all")

rad1 = 0.5  #Core radius[um]
D1 = np.loadtxt("CylindricalShell_5Layer_cSi_radius0.5um.txt", delimiter=",", skiprows=3)
lam = D1[:,0] * 1e9 #wavelength[nm]
T1 = D1[:, 1]
R1 = -T1
Rm1 = np.max(R1)

rad2 = 1.0
D2 = np.loadtxt("CylindricalShell_5Layer_cSi_radius1.0um.txt", delimiter=",", skiprows=3)
T2 = D2[:, 1]
R2 = -T2
Rm2 = np.max(R2)

rad3 = 1.5
D3 = np.loadtxt("CylindricalShell_5Layer_cSi_radius1.5um.txt", delimiter=",", skiprows=3)
T3 = D3[:, 1]
R3 = -T3
Rm3 = np.max(R3)

rad4 = 2.0
D4 = np.loadtxt("CylindricalShell_5Layer_cSi_radius2.0um.txt", delimiter=",", skiprows=3)
T4 = D4[:, 1]
R4 = -T4
Rm4 = np.max(R4)

rad5 = 2.5
D5 = np.loadtxt("CylindricalShell_5Layer_cSi_radius2.5um.txt", delimiter=",", skiprows=3)
T5 = D5[:, 1]
R5 = -T5
Rm5 = np.max(R5)


pl.figure(1)
pl.plot(lam, R1, label = "o.5um")
pl.plot(lam, R2, label = "1.0um")
pl.plot(lam, R3, label = "1.5um")
pl.plot(lam, R4, label = "2.0um")
pl.plot(lam, R5, label = "2.5um")
pl.xlabel("wavelength[nm]")
pl.ylabel("R")
pl.legend()


rad = [rad1, rad2, rad3, rad4, rad5]
Rm = [Rm1, Rm2, Rm3, Rm4, Rm5]

pl.figure(2)
pl.plot(rad, Rm)
pl.xlabel("Core Radius[um]")
pl.ylabel("Rmax")