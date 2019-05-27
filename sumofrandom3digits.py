from random import random

n = random() * 900 +100
n=int(n)
print (n)

print("Addition of digits in a number")
a=0

153

a+=n//100
n=n%100

a+=n/10
a+=n%10
a=int(a)

print(a)
