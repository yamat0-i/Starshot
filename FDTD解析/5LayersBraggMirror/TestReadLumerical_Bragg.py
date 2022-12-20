#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:31:26 2022

@author: mark
"""

# Test lumerical reader

import numpy as np
import matplotlib.pyplot as pl
import ReadLumerical_Bragg as rl

# Clean up plot space
pl.close("all")

# Read in data
# x, y, datazy = rl.ReadLumericalDataFile2D('5LayersBraggMirror_cSi_0.3-1.5um_v3.txt')

# Plot
#pl.figure(1)
#pl.pcolor(x*1e6,y*1e6,datazy.T)

# Read in data
#y, z, datazy = rl.ReadLumericalDataFile2D('Lambda660nm_Intensity_AlongZAxis.dat')

# Plot
#pl.figure(2)
#pl.pcolor(z*1e6,y*1e6,datazy)

# 1D
# pl.figure(3)
# dataslice = datazy[20,:]
# pl.plot(z*1e6,dataslice)


D = np.loadtxt('5LayersBraggMirror_cSi_0.3-1.5um_v3.txt', delimiter=",", skiprows=3)
lam = D[:,0]
I = D[:,1]

pl.plot(lam,I)

