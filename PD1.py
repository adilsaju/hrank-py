from math import factorial
import math

lam = 2.5
k = 5

p = lam**k*math.exp(-lam)/factorial(k)
print(p)