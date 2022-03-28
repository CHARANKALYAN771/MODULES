import numpy as n
x=n.array([1,2,3,], ndmin=5)
print((x.ndim))
x=n.array([[1,2,3],[4,5,6,]])
print(x[1][2])
x=n.array([1.3,2.4,3.2,4.3,5.1])
print(x.dtype)
y=x.astype('i')
print(y)
v=n.random.randint(1,10)
print(v)
y=n.random.randint(100, size=(2,5))
print(y)

arr = n.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
x=n.array([])
for i in arr:
    print(i)
         
print(x)

for i in n.nditer(arr):
    if i%2==0:
        print(i)

x=n.random.randint((100) , size=(2,5) )
print(x.astype(float))
print(x)

x=[1,2,3,4,5]
print(type(x))
y=n.array(x)
print(n.lcm.reduce(y))

import numpy as n
arr = n.array([[1,2,3],[4,5,6,],[7,8,9]])
# print(arr)

for i in n.arange(1,10):
    print(i)

for i in n.nditer(arr):
    print(i)

print(arr[0:3,1])

x=n.array([2,3,4,])
y=n.array([4,5,6])
print(x.astype(float))

print(n.vstack((x,y)))
print(n.hstack((x,y)))

res=n.array_split(x,4)
print(res)

from numpy import random
import random as r
print(n.random.randint(100,size=(2,5)))

x=123
y=[]
while(x>0):
    y.append(x%10)
    x//=10
y.reverse()

arr=n.array(y)
p=2**len(y)
t=1
while(t<p):
    print(n.random.permutation(y))
    t+=1
