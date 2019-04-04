# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:00:54 2019

@author: Miriam
"""

#Using the Box-Müller Method to generate 2-dimensionally normally distributed variables

import numpy as np
import matplotlib.pyplot as plt

#For mu = (0,0), covariance matrix Sigma = identity matrix

n = 500 #Number of random numbers
a = np.random.exponential(scale=1,size=n)
phi = np.random.uniform(low=0,high = 2*np.pi,size=n)

#change to carthesian coordinates
x = a * np.cos(phi)
y = a * np.sin(phi)

plt.figure(1)
plt.plot(x,y, 'ro')

#For Covariance matrix sigma = A: Y = X/sqrt(Sigma) ~ N(0,I) => Y*sqrt(Sigma)

# Calculate sqrt(A) with Jordan decomposition
A=[[3,1],[1,1]]
A_eig=np.linalg.eig(A)
E_val=A_eig[0]
Gamma=A_eig[1]
Lambda=np.diag(E_val)
np.sqrt(Lambda)
Lambda12 = np.sqrt(Lambda)
A12=np.dot(np.dot(Gamma,Lambda12),np.transpose(Gamma))

#Solve with matrix multiplication
c = [x,y]
N = np.dot(A12,c) 

#print(N)
plt.figure(2)
plt.plot(N[0],N[1], 'ro')