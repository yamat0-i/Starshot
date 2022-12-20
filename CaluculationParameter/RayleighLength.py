# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:57:39 2022

@author: 81809
"""

import matplotlib.pyplot as pl
import numpy as np

om0 = np.linspace(1e-3, 10, 100000) # Beam waist
lam = 1e-6 # Wavelength [m]
zR = np.pi * om0**2 / lam # Rayleigh length [m]



pl.figure(4)
pl.plot(om0, zR)
pl.xlabel("Beam waist [m]")
pl.ylabel("Rayleigh length [m]")
pl.yscale("log")