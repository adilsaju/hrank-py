# from math import factorial
# import math

lam1 = .88
lam2 = 1.55
# k = 1
# x = lam1**k*math.exp(-lam1)/factorial(k)
# y = lam2**k*math.exp(-lam2)/factorial(k)

Eca = 160+40*(lam1+lam1**2)
Ecb = 128+40*(lam2+lam2**2)
print(f'{Eca:.3f}')
print(f'{Ecb:.3f}')
