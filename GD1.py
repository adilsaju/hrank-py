# GEOMETRIC DISTRIBUTION
p=1/3
q=1-p
# n=5
a=0
for n in range(1,6):
    a+=p*q**(n-1)
print(f'{a:.3f}')