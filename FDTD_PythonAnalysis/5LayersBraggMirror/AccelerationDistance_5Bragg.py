# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:10:53 2022

@author: 81809
"""

from scipy import integrate
import matplotlib.pyplot as pl
import numpy as np
import sympy as sy
import ReadLumerical_Bragg as rl

"""
D = np.loadtxt('5LayersBraggMirror_cSi_0.3-1.5um_v3.txt', delimiter=",", skiprows=3)
lam = D[:,0]
T = D[:,1]
R = -np.average(T) #Rreflectance of the sail
print(R)
"""

#Parameter
c = 3.0e8 #Light speed
v_f = 0.1 * c #Desired velocity
I = 1e-3#Laser intensity[W / m^2]
A = 10#Area of the sail[m^2]
m_s = 1.3e-2#Mass of sail[kg]
m_p = 1e-4 #Mass of payload[kg]
m_t = m_s + m_p #Total mass of the spacecraft
R = 1 #Reflectance of the sail

#Integral calculation
def f(v):
    
    beta = v / c
    gam = 1 / np.sqrt(1 - beta**2) #Lorentz factor

    return m_t * gam * v / (R * (1 - beta)**2)
v = np.linspace(0,3e8,1000)
pl.plot(v,f(v))

"""
a = int(input(0)) #Lower limit
b = int(input(v_f)) #Upper limit

ans,err = integrate.quad(f, a, b)

print("ans")
print(ans)
print("err")
print(err)

#Calculation of D
D = (c / (2 * I * A)) * ans #Acceleration distance

print("D")
print(D)
"""