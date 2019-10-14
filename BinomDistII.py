from math import factorial as fact
p=.12
q=.88
# print(p)
b1=0;b2=0;n=10
for i in range(0,3):
    b1+=fact(n)/fact(n-i)/fact(i)*p**i*q**(n-i)
for i in range(2,11):
    b2+=fact(n)/fact(n-i)/fact(i)*p**i*q**(n-i)

print(f'{b1:.3f}\n{b2:.3f}')