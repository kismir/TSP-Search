import numpy
import random
from math import floor,sqrt
from itertools import combinations,permutations
from matplotlib import pyplot as plt

def MGen(n=5,h=100,w=100):
    cou=0
    lst=[]
    while cou < n:
        cou+=1
        x,y=floor(random.random()*h),floor(random.random()*h)
        if (x,y) not in lst:
            lst.append((x,y))
    print(lst)
    comb=combinations(lst,2)
    #b=list((comb))
    #print(b)
    M3=numpy.zeros((n,n))
    l=[]
    for line in comb:
        ln=numpy.array(line)
        z=numpy.linalg.norm(ln[1]-ln[0])
        l.append(z)

    cou=0
    for i in range(n-1):
        for j in range(n-i-1):
            M3[i][i+j+1]=l[cou]
            cou+=1
    A=M3+M3.transpose()
    return lst,A

def GenMBySeq(M,seq):
    l=len(M)
    A=numpy.zeros((l,l))
    for i in range(l):
        for k,j in enumerate(seq):
            A[i][k]=M[seq[i]][j]
    return A

def Nsolve(M):
    l=len(M)
    lst=range(l)

    c=permutations(lst,l)
    summ=float('inf')
    win=[]
    for i in c:
        NM=GenMBySeq(M,i)
        #print(M)
        #print(NM)
        
        s=NM[0][1]+NM[0][-1]
        #print(NM[0][1],NM[0][-1])
        for j in range(1,l-1):
            s+=NM[j][j+1]
            #print(NM[j][j+1])
        #print(s)
        if summ>s:
            #print('yes')
            summ=s
            win=i
        #print('###########################')

    return win

#####################
#       Body        #
#####################

h,w=100,100
n=9
lst,M=MGen(n,h,w)
print(M)
print(lst)
res=Nsolve(M)
print(res)

x=[]
y=[]
for i in res:
    x.append(lst[i][0])
    y.append(lst[i][1])
x.append(lst[res[0]][0])
y.append(lst[res[0]][1])
plt.plot(x,y)
plt.show()
    

    
    
