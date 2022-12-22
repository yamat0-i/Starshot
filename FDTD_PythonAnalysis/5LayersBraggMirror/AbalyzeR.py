# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:27:49 2022

@author: 81809
"""

import numpy as np
import matplotlib.pyplot as pl

# Clean up plot space
pl.close("all")

D = np.loadtxt('ファイル名', delimiter=",", skiprows=3)
lam = D[:,0]
T = D[:,1]
R = -T #Rreflectance of the sail
print(R)

pl.figure()
pl.plot(lam, R)
pl.xlabel("lam[m]")
pl.ylabel("R")
pl.title("タイトル")