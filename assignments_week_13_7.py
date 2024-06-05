# -*- coding: utf-8 -*-
"""Assignments Week 13 - 7

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19WbzX3o6ZXGf9itZJlQ2JF4VPp1f6EiD
"""

import numpy as np

def costf(w, x, y):
  yp = w.T@x
  return(yp-y.T)@(yp-y.T).T

def gradJ(w):
  return np.array([8*w[0]+4*w[1]+4*w[2]-4, 4*w[0]+4*w[1]+2*w[2]-4, 4*w[0]+2*w[1]+4*2-4])

def step_func(x):
    y = x>0
def step_func(y):
    return 2*y.astype(int)-1

xi = np.array([[1,1,1,1], [0,1,0,1],[0,0,1,1]])
yi = np.array([[-1],[1],[1],[1]])
wi = np.array([[0],[0],[0]])

alpha = 0.01
J = costf(wi, xi, yi)

while(True):
  JP = J
  delw = alpha*gradJ(wi)
  wi = wi - delw
  J = costf(wi, xi, yi)
  print(J, wi.T)
  if(np.abs(J-JP)/J) < 0.000001: break

print(wi)