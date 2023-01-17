# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:34:27 2022

@author: markt
"""

import numpy as np
import matplotlib.pyplot as pl

pl.close("all")

rad1 = 0.5  #Core radius[um]
<<<<<<< HEAD
D1 = np.loadtxt("CylindricalShell_5Layer_radius0.5um.txt", delimiter=",", skiprows=3)
=======
D1 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius0.5um.txt", delimiter=",", skiprows=3)
>>>>>>> origin/master
lam = D1[:,0] * 1e9 #wavelength[nm]
T1 = D1[:, 1]
R1 = -T1
Rm1 = np.max(R1)

rad2 = 1.0
<<<<<<< HEAD
D2 = np.loadtxt("CylindricalShell_5Layer_radius1.0um.txt", delimiter=",", skiprows=3)
=======
D2 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius1.0um.txt", delimiter=",", skiprows=3)
>>>>>>> origin/master
T2 = D2[:, 1]
R2 = -T2
Rm2 = np.max(R2)

rad3 = 1.5
<<<<<<< HEAD
D3 = np.loadtxt("CylindricalShell_5Layer_radius1.5um.txt", delimiter=",", skiprows=3)
=======
D3 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius1.5um.txt", delimiter=",", skiprows=3)
>>>>>>> origin/master
T3 = D3[:, 1]
R3 = -T3
Rm3 = np.max(R3)

rad4 = 2.0
<<<<<<< HEAD
D4 = np.loadtxt("CylindricalShell_5Layer_radius2.0um.txt", delimiter=",", skiprows=3)
=======
D4 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius2.0um.txt", delimiter=",", skiprows=3)
>>>>>>> origin/master
T4 = D4[:, 1]
R4 = -T4
Rm4 = np.max(R4)

rad5 = 2.5
<<<<<<< HEAD
D5 = np.loadtxt("CylindricalShell_5Layer_radius2.5um.txt", delimiter=",", skiprows=3)
=======
D5 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius2.5um.txt", delimiter=",", skiprows=3)
>>>>>>> origin/master
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
<<<<<<< HEAD
=======
pl.title("Cylindrical Shell (MoS2)")
>>>>>>> origin/master
pl.legend()


rad = [rad1, rad2, rad3, rad4, rad5]
Rm = [Rm1, Rm2, Rm3, Rm4, Rm5]

pl.figure(2)
pl.plot(rad, Rm)
pl.xlabel("Core Radius[um]")
<<<<<<< HEAD
pl.ylabel("Rmax")
=======
pl.ylabel("Rmax")
pl.title("Cylindrical Shell (MoS2)")
>>>>>>> origin/master
