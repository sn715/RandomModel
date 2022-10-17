import numpy as np

def fct_1(a, b):
  c = a+b
  d = np.mean([a,b,c])
  return a, b, c, d
