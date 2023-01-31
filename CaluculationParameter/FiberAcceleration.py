#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 09:56:28 2022

@author: mark
"""

import numpy as np

P = 1e-3
rho = 19300 # Density of gold in kg / m^3 
r = 1e-9
m = rho * 4/3 * np.pi * r**3
c = 2.99e8
t = 0.001
a = 2 * P / (m * c)
v = a * t
d = 0.5 * a * t ** 2

print("Velocity")
print(v/c)
print("Distance") 
print(d)

