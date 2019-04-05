#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:31:27 2019

@author: haerdle1
"""

# Using the Box-Mueller Method to generate 2-dim normally distributed variables

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100) # Set seed from comparability

# For mu = (0,0), covariance matrix Sigma = identity matrix
n = 500 # Number of random numbers
msize = 0.1 # determines the size of the plotted points
# a good size might be msize=5 for n=500 pts and misze=0.1 for n>50K  
a = np.random.exponential(scale=1,size=n)
phi = np.random.uniform(low=0,high = 2*np.pi,size=n)

# change to cartesian coordinates
x = a * np.cos(phi)
y = a * np.sin(phi)

plt.figure(figsize=(4,4))
plt.plot(x,y, 'ro', markersize=msize)

# for Covariance matrix Sigma = A: Y = X/sqrt(Sigma) ~ N(0,I) => Y*sqrt(Sigma) ~ N(0,Sigma)

# Calculate sqrt(A) with Jordan decomposition
A=[[3,1],[1,1]]
A_eig=np.linalg.eig(A)
E_val=A_eig[0]
Gamma=A_eig[1]
Lambda=np.diag(E_val)
np.sqrt(Lambda)
Lambda12 = np.sqrt(Lambda)
A12=np.dot(np.dot(Gamma,Lambda12),np.transpose(Gamma))

# Solve with matrix multiplication
c = [x,y]
tfxy = np.dot(A12,c) 

# print(tfxy)
plt.figure(2,figsize=(6,4))
plt.plot(tfxy[0],tfxy[1], 'ro', markersize=msize)
