# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:19:04 2022

@author: markt
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up
pl.close("all")

# SiO2
rad = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8]
fileroot = "T_SiO2_radius"

R = np.zeros(np.shape(rad))
for ll in np.arange(len(rad)):
    Data = np.loadtxt(fileroot+"%1.1f.txt"%rad[ll],skiprows = 3, delimiter=",")
    print("Loaded values:")
    print(Data)
    R[ll] = Data[1]

pl.figure(1)    
pl.plot(rad,np.abs(R),'.-')
pl.xlabel("Radius (um)")
pl.ylabel("R")    
pl.title("SiO2")
pl.savefig("SiO2_Refelction.png")


# Au
rad = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8]
fileroot = "T_Au_radius"

R = np.zeros(np.shape(rad))
for ll in np.arange(len(rad)):
    Data = np.loadtxt(fileroot+"%1.1f.txt"%rad[ll],skiprows = 3, delimiter=",")
    print("Loaded values:")
    print(Data)
    R[ll] = Data[1]

pl.figure(2)    
pl.plot(rad,np.abs(R),'.-')
pl.xlabel("Radius (um)")
pl.ylabel("R")    
pl.title("Au")
pl.savefig("Au_Refelction.png")


