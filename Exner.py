#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 14:17:15 2017

@author: livbeaulieu30
"""
import numpy as np
from matplotlib import pyplot as plt

#exner Equation model 

#Variables
n = 1. * np.arange(1000, -1, -10) #bed elevation relative to some fixed datum
dt = .1 #time (seconds)
e = 0.6 #bed porosity
x = 1000. * np.arange(len(n)) #downstream distance (100km)
dx = np.mean(np.diff(x)) # because it is regularly-spaced

# Boundary conditions: Dirichlet -- already set in input
n[0] = 990.
n[-1] = 0.

# Constants
rho_s = 2.65
rho_f = 1.
D50 = 0.05
g = 9.8
h = 100

 

#fig = plt.figure()
#plt.plot(x, n, 'r-', linewidth=2)

plt.plot( x, n, 'k-', linewidth=2)
# Run for 100 time steps
for i in range(int(10)):
    dn = np.diff(n)
    #dx = np.diff(x)
    tau_b = (rho_f * g * h * (-dn / dx))
    tau_c = 0.0495 * (rho_s - rho_f) * g * D50
    qs = 4 * (tau_b - tau_c \
         / (((rho_s / rho_f) * g)))** 1.5 * \
         (((rho_s / rho_f) - 1) * g) #sediment flux
    qs[tau_b < tau_c] = 0 # no sed flux
    dqs = np.diff(qs)
    dn_dt = -1/e * dqs / dx
    n[1:-1] = n[1:-1] + dn_dt * dt


#plt.plot( (x[:-1] + x[1:])/2., qs, 'b-', linewidth=2)
plt.plot( x, n, 'b-', linewidth=2)

plt.xlabel('Downstream Distance')
plt.ylabel('Bed Elevation')
plt.title('Exner Equation Model')

plt.show()
