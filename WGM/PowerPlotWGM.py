# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:40:56 2023

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit

#Clean Up
pl.close("all")

#Load Data
D = np.loadtxt("WGM_SiO2.txt", delimiter = ",", skiprows = 3)
rad = D[:, 0]
P = D[:, 1]

#Plot
pl.figure()
pl.plot(rad, P)
pl.show()