# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 07:36:27 2018

@author: josep
"""

import numpy as np
a = np.random.randn(5)
print (a)
print(a.shape)
print(a.T)
print(np.dot(a,a.T))
a = np.random.randn(5,1)
print(a)
print(a.T)
print(np.dot(a,a.T))
