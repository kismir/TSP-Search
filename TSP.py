import numpy
from random import random
from math import floor,sqrt
from itertools import combinations,permutations
from matplotlib import pyplot as plt
from GenSearch import *

def MGen(n=5,h=100,w=100):
    cou=0
    lst=[]
    while cou < n:
        x,y=floor(random()*w),floor(random()*h)
        if (x,y) not in lst:
            cou+=1
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

def GenSBySeq(M,seq):
    l=len(M)
    NM=GenMBySeq(M,seq)
    s=NM[0][1]+NM[0][-1]
    #print(NM[0][1],NM[0][-1])
    for j in range(1,l-1):
        s+=NM[j][j+1]
    return s
    
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

def Rselection(best,a1):
        cbest=best[:]
        x1=floor(random()*len(cbest))
        x2=floor(random()*len(cbest))
        x=sorted((x1,x2))
        gen=a1[x[0]:x[1]]
        if random()<0.5:
            gen=list(reversed(gen))
        if len(gen)>2:
            for i in gen:
                ind=cbest.index(i)
                cbest.remove(i)
            cbest[ind:ind]=gen
        
        return cbest

def CebCheck(M,bsol):
    best=bsol[0][:]
    for o in range(3): 
        for i in range(len(best[:-1])):
            r=bsol[0][:]
            r[i]=bsol[0][i+1]
            r[i+1]=bsol[0][i]
            score=GenSBySeq(M,r)
            if bsol[1]>score:
                bsol=(r[:],score)
    return bsol

def evolveSolve(M,pop):

    n=len(M)
    count=len(pop)#160
    #a=list(range(n))
    #a=np.arange(n)
    #print(a)
    iterations=1500#1000
    mutproc=1/n#best choice
    mutchance=1 # best choice
    wproc=0.01
    CheckTimer=list(takewhile(lambda x : x< iterations, (i**7 for i in range(iterations))))

    ### Start evolve ###
    best=float('inf')
    w=[]
    for iterat in range(iterations):

        ### mutate & selection

        scores=[]
        mutants=[]
        for u,individ in enumerate(pop):
            if u!=0:
                mutant=mutate(individ,mutproc,mutchance)
            else:
                mutant=individ
            mutants.append(mutant)
            score=GenSBySeq(M,mutant)
            #print(a,mutant,score)

            scores.append(score)
        
        topv=floor(count*wproc)

        wlist=sorted(scores)[:topv]
        print(iterat,' iteration, best score : ',wlist[0])
        w.append(wlist[0])
        winners=[]
        flag=0
        for k,i in enumerate(scores):
            if i ==0:
                print('done ',mutants[k])
                flag=1
            if i in wlist:
                winners.append(mutants[k])
                if i==wlist[0]:
                    best=mutants[k]
                    bsol=(best,wlist[0])
                    if iterat == (iterations-CheckTimer[-1]):
                        CheckTimer.pop()
                        bsol=CebCheck(M,bsol)
                        best=bsol[0]
                        print('ok')
                        

        if flag==1:
            break
              
        ### breed
        pop=[best]
        for i in range(count-1):
            a1=choice(winners)
            child=Rselection(best,a1)
            pop.append(child)

    print(best)

    ### control check ###
    print('control check')
    #bsol=(best,wlist[0])
    bsol=CebCheck(M,bsol)

    #print(bsol[0],bsol[1])

    return bsol[0]

#####################
#       Body                          #
#####################

h,w=100,100
n=50
lst,M=MGen(n,h,w)
#print(M)
print(lst)
#res=Nsolve(M)
#print(res)

pop=genPop(list(range(n)),100)
res=evolveSolve(M,pop)

x=[]
y=[]
for i in res:
    x.append(lst[i][0])
    y.append(lst[i][1])
x.append(lst[res[0]][0])
y.append(lst[res[0]][1])
plt.plot(x,y)
plt.show()
    

    
    
