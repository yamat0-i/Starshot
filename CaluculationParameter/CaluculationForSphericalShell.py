# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:25:03 2022

@author: 81809
"""


import matplotlib.pyplot as pl
import math
import numpy as np



#Calculate thickness of sail
#c-Si(index = 3.35)

M = 1e-9 #Mass of sail[kg]
rho = 2330 #Density [kg/m^3]
d = 1e-6 #thickness[m]
r = math.sqrt(M / (4* np.pi* d* rho)) #radius[m]

print(r)

#pl.figure(1)
#pl.plot(r,d)
#pl.yscale("log")
#pl.ylabel("Thickness[m]")
#pl.xlabel("Radious[m]")
#pl.title("Thickness c-Si")

