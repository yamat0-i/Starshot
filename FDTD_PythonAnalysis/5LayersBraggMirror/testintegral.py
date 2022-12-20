# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:57:22 2022

@author: 81809
"""

import numpy as np
import sympy as sy

v = sy.Symbol('v')
c = sy.Symbol('c')

f = sy.Function('f')

f = ((1 - v**2 / c**2)**(-1/2)) * v / ((1 - v / c)**2)

print(f)

I = integrate(f, v)

print(I)
print("Finished!")