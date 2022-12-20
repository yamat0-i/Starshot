# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 01:49:48 2022

@author: User
"""

import matplotlib.pyplot as pl
import math
import numpy as np

#Calculate thickness of sail
#Au
M = 1e-9 #Mass of sail[kg]
rho1 = 19320 #Density [kg/m^3]
d = np.linspace(10e-10, 10e-5, 1000000) #thickness[m]
r1 = (M / (4 * np.pi * rho1 *d))**(1/2) #radious[m]

#pl.figure(1)
#pl.plot(d,r1)
#pl.xscale("log")
#pl.xlabel("Thickness[m]")
#pl.ylabel("Radious[m]")
#pl.title("Radious Au")

#Ag
M = 1e-9 #Mass of sail[kg]
rho2 = 10490 #Density [kg/m^3]
d = np.linspace(10e-10, 10e-5, 1000000) #thickness[m]
r2 = (M / (4 * np.pi * rho2 *d))**(1/2) #radious[m]

#pl.figure(2)
#pl.plot(d,r2)
#pl.xscale("log")
#pl.xlabel("Thickness[m]")
#pl.ylabel("Radious[m]")
#pl.title("Radious Ag")

#Al
M = 1e-9 #Mass of sail[kg]
rho3 = 2698 #Density [kg/m^3]
d = np.linspace(10e-10, 10e-5, 1000000) #thickness[m]
r3 = (M / (4 * np.pi * rho3 *d))**(1/2) #radious[m]

#Si3N4
m = 1e-12 #Mass of sail[kg]
rho4 = 3440 #Density [kg/m^3]
d = np.linspace(10e-10, 10e-5, 1000000) #thickness[m]
r4 = (m / (4 * np.pi * rho4 *d))**(1/2) #radious[m]

#BN
m = 1e-12 #Mass of sail[kg]
rho5 = 3487 #Density [kg/m^3]
d = np.linspace(10e-10, 10e-5, 1000000) #thickness[m]
r5 = (m / (4 * np.pi * rho5 *d))**(1/2) #radious[m]

pl.figure(3)
pl.plot(d, r1, label="Au", color="gold")
pl.plot(d, r2, label="Ag", color="silver")
pl.plot(d, r3, label="Al", color="skyblue")
pl.xscale("log")
pl.xlabel("Thickness[m]")
pl.ylabel("Radious[m]")
#pl.title("Radious")
pl.legend()

pl.figure(4)
pl.plot(d, r4, label="Si3N4", color="gold")
pl.plot(d, r5, label="BN", color="silver")
#pl.plot(d, r3, label="Al", color="skyblue")
pl.xscale("log")
pl.xlabel("Thickness[m]")
pl.ylabel("Radious[m]")
#pl.title("Radious")
pl.legend()