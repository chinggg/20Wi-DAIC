import numpy as np
a=np.array([10,20,30,40,50,0])

print(a[0])

print(a[1:4])

print(a[a > 20])

print(a[(a >=20)&(a <=50)])

a[2]=1000
print(a)

a[-1]-=10
print(a)

