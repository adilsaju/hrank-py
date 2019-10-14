from math import factorial as fact
p=1.09/2.09
# print(p)
b=0
for i in range(3,7):
    b+=fact(6)/fact(6-i)/fact(i)*p**i*(1-p)**(6-i)
print(b)
print(f'{b:.3f}')