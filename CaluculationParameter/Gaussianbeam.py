# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:25:12 2022

@author: yuu42
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:29:00 2022

@author: marks
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 13:11:37 2018

@author: mark
"""

# Implement the classical cavity "QED" model of Novotny 
# from his paper "Strong coupling, energy splitting, and level crossings: A classical
# perspective", Am. J. Phys. 78 1199 (2010)
#
# In this case, we show the Purcell regime, where the electron oscillation decays at a rate close 
# to the cavity decay rate.

from scipy.integrate import ode
import matplotlib.pyplot as pl
import numpy as np

def a(z):
    # m = 6.28*10**(-19)
    # p = 1.0*10**(-3)
    # c = 3.0*10**8
    # q = 400*10**(-9)
    # r = 25*10**(-9)
    
    rho = 2700 # Density [kg / m^3]
    m = 1e-3 #Mass of particle [kg]
    #m = 4 / 3 * r**3 * rho*np.pi # Mass of particle
    da = 2e-4 #Areal density [kg / m^2]
    r = (m / (8 * np.pi * 1e-4))**(1/2) # Radius of nanoparticle [m]
    P0 = 70e9 # Optical power [W]
    c = 2.99e8 # Speed of light [m / s]
    lam = 1e-6 # Wavelength [m]
    
    print(r)
    
    om0 = 2 # Beam waist
    zR = np.pi * om0**2 / lam # Rayleigh length
    om = om0 * np.sqrt(1 + (z / zR)**2) # Beam waist at position z
    I0 = P0 / (np.pi * om0**2) # Intensity at beam waist
    #I = I0 * (om0 / om)**2 * np.exp(-2 * r**2 / (om**2)) # Intensity at particle radius
    P = P0 * (1 - np.exp(-r**2 / om**2)) # Approximate power of beam within particle radius
    
    acc = 2 * P / (m * c)
    
    return acc


# Define the right hand side (RHS) of the differential equation 
# used to model the coupled oscillators.
def RHS(t, u, p):
    # u = [z,
    #      v]
    # z = u[0]
    # v = u[1]
    


    f = [u[1],
         a(u[0])]
    
    return f

# Clean up plot
pl.close("all")

# Parameters
c = 2.99e8 # Speed of light [m / s]


# Set up integrator for complex values
r = ode(RHS, jac=None).set_integrator('vode', method='bdf')

# Initial conditions
u0 = [0.0, 0.0]
r.set_initial_value(u0, t=0.0).set_f_params(0)

print("Here")
# Set up variables to hold the output
u = []
t = []

# Define intergration parameters
T = 1e5 # Total time in arb. units
dt = T / 100000 # Time step at which to sample the dynamics

# Perform the integration to numerically solve the D.E.s
while r.successful() and r.t <= T:
    r.integrate(r.t + dt)
    u.append(r.y)
    t.append(r.t)

# Display results
u = np.array(u)
pl.figure(1)
pl.clf()
pl.plot(t,np.real(u[:,0]) * 1e3,'r-', label = "z")
#pl.plot(t,np.real(u[:,1]),'b-', label = "v")
pl.xticks(fontsize=16)
pl.yticks(fontsize=16)
pl.xlabel("t (s)",fontsize=18)
pl.ylabel("z (mm)",fontsize=18)
pl.xscale("log")
#pl.title("gamma = %1.2f, kappa = %1.2f, g = %1.2f"%(gamma,kappa,g),fontsize=18)
pl.tight_layout()
pl.legend()

pl.figure(2)
pl.clf()
#pl.plot(t,np.real(u[:,0]),'r-', label = "z")
pl.plot(t,np.real(u[:,1])/c,'b-', label = "v")
pl.xticks(fontsize=16)
pl.yticks(fontsize=16)
pl.xlabel("t (s)",fontsize=18)
pl.ylabel("v/c ",fontsize=18)
pl.xscale("log")
#pl.yscale("log")
#pl.title("gamma = %1.2f, kappa = %1.2f, g = %1.2f"%(gamma,kappa,g),fontsize=18)
pl.tight_layout()
pl.legend()

pl.figure(3)
pl.clf()
z = np.linspace(0,10e-6,100)
pl.plot(z * 1e6,a(z),'r')
pl.xlabel("Distance from beam waist (um)")
pl.ylabel("Acceleration (m / s^2)")
pl.xscale("log")
pl.show()

