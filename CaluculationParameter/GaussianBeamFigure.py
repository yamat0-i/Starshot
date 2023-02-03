# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:54:52 2023

@author: 81809
"""

#https://www.fiberoptics4sale.com/blogs/wave-optics/gaussian-beam
#↑の図っぽいものを作ろうとした
#ガウス分布のサイズ要調整
#あと色

import numpy as np
import matplotlib.pyplot as pl

#clean up
pl.close("all")

#gaussian distribution
sig = 0.5
mu = 0    #0で固定
x = np.linspace(-10, 10, 1000)

g = np.exp(-(x - mu)**2 / 2 * sig**2) / np.sqrt(2 * np.pi * sig**2) - 6

pl.figure(1)
pl.plot(g, x, color = "blue")
pl.show()

#spot size
z = np.linspace(-6, 6, 100)
w0 = 4
lam = 1
#zR = np.pi * w0**2 / lam
zR = 2
w1 = w0 * np.sqrt(1 + (z / zR)**2)
w2 = -w1

pl.figure(1)
pl.plot(z, w1, color = "red")
pl.plot(z, w2, color = "red")
pl.axhline(y = 0, xmin = 0, xmax = 10, color = "black") #z軸
pl.xlabel("z")
pl.ylabel("w")
