# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:58:16 2023

@author: 81809
"""

import numpy as np

rad6 = 0.5  #Core radius[um]
D6 = np.loadtxt("CylindricalShell_5Layer_MoS2_radius0.5um.txt", delimiter=",", skiprows=3, max_rows=13)
lam = D6[:,0] * 1e9 #wavelength[nm]
T6 = D6[:, 1]
R6 = -T6
Rm6 = np.max(R6)

lam6 = D6[6, 0]
R6a = -D6[6, 1]

print(lam6)
print(R6a)