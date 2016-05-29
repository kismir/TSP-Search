import numpy
import random
from math import floor,sqrt
from itertools import combinations
h,w=100,100
n=5
cou=0
lst=[]
while cou < n:
    cou+=1
    x,y=floor(random.random()*h),floor(random.random()*h)
    if (x,y) not in lst:
        lst.append((x,y))
print(lst)
comb=combinations(lst,2)
#print (list(comb))
M3=numpy.zeros((n,n))
l=[]
for line in comb:
    ln=numpy.array(line)
    z=numpy.linalg.norm(ln[1]-ln[0])
    l.append(z)

cou=0
for i in range(n-1):
    for j in range(n-i-1):
        M3[i][n-j-1]=l[cou]
        cou+=1
A=M3+M3.transpose()
print(A)
    
    

    
    
