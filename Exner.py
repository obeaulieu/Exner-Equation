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
n = 1. * np.arange(100) #bed elevation relative to some fixed datum
n[0] = 1000.
n[-1] = 0.
dt = 1E4 * 3.15E7 #time (years)
e = 0.6 #bed porosity
x = 1000. * np.arange(100) #downstream distance (100km)

rho_s = 2.65
rho_f = 1.
D50 = 0.05
g = 9.8
h = 100

 

#fig = plt.figure()
#plt.plot(x, n, 'r-', linewidth=2)

# Run for 100 time steps
for i in range(int(10000)):
    dn = np.diff(n)
    dx = np.diff(x)
    qs = 4 * (((rho_f * g * h * (dn / dx)) - (0.495 * (rho_s - rho_f) * g * D50)) / (((rho_s / rho_f) * g)) ** 1.5) * (((rho_s / rho_f) - 1) * g) #sediment flux
    dqs = np.diff(qs)
    dn_dt = dqs / dx


plt.plot(dx, qs, 'b-', linewidth=2)

plt.show()
