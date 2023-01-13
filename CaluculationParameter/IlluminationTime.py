# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:24:32 2022

@author: User
"""

import matplotlib.pyplot as pl
import math
import numpy as np


#Calculation of illumination time
R = 1 #Reflectance
P1 = 1e-3
P2 = 10e-3 #Power[W]
v = 10e+3 #Velocity gain [m/s]
c = 3e+8 #Speed of light [m/s]
M = np.linspace(1e-7, 1e-2, 10000) #Mass of sail[g]
t1 = (v * c * M) / (2 * R * P1) * 10e-3
t2 = (v * c * M) / (2 * R * P2) * 10e-3 #Time[s]
y1 = t1 / (365 * 24 * 60 * 60)
y2 = t2 / (365 * 24 * 60 * 60) #Time[year]

pl.figure(1)
pl.plot(M, t1, label="1mW")
pl.plot(M, t2, label="10mW")
pl.xscale("log")
pl.yscale("log")
pl.xlabel("M[g]")
pl.ylabel("t[s]") 
pl.title("Illumination Time(second)")
pl.legend()

pl.figure(2)
pl.plot(M, y1, label="1mW")
pl.plot(M, y2, label="10mW")
pl.xscale("log")
pl.yscale("log")
pl.xlabel("M[g]")
pl.ylabel("t[year]") 
pl.title("Illumination Time(year)")
pl.legend()

#Calculation of mass of sail
#r1 = #Inner diameter
#r2 = #Outer diameter
#r = r1 - r2
#rho = #Dencity
#M = 4* np.pi* r**3* rho / 3