from random import shuffle,random,choice
from math import floor
import time
import numpy as np
from itertools import count,takewhile

def genPop(a,count):
    b=a[:]
    z=[]
    for i in range(count):
        shuffle(b)
        z.append(b[:])

    return z

def mutate(obj,proc,mutchance):
    l=len(obj)
    n=floor(proc*l)
    res=obj[:]
    if random()<mutchance:
        for i in range(n):
            r1=floor(random()*l)
            r2=floor(random()*l)
            res[r2]=obj[r1]
            res[r1]=obj[r2]
            obj=res[:]        
            
    return res

def selection(best,a1):
        cbest=best[:]
        x1=floor(random()*len(cbest))
        x2=floor(random()*len(cbest))
        x=sorted((x1,x2))
        gen=a1[x[0]:x[1]]
        if len(gen)>2:
            for i in gen:
                ind=cbest.index(i)
                cbest.remove(i)
            cbest[ind:ind]=gen
        
        return cbest

def GetScore(a,mutant):
    score=0
    for k,i in enumerate(mutant):
        score+=abs(a[k]-i)
    return score

def CCheck(bsol):
    best=bsol[0][:]
    for o in range(3): 
        for i in range(len(best[:-1])):
            r=bsol[0][:]
            r[i]=bsol[0][i+1]
            r[i+1]=bsol[0][i]
            score=GetScore(a,r)
            if bsol[1]>score:
                bsol=(r[:],score)
    return bsol

def evolve(a,pop):

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
            score=GetScore(a,mutant)
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
                        bsol=CCheck(bsol)
                        best=bsol[0]
                        print('ok')
                        

        if flag==1:
            break
              
        ### breed
        pop=[best]
        for i in range(count-1):
            a1=choice(winners)
            child=selection(best,a1)
            pop.append(child)

    print(best)

    ### control check ###
    print('control check')
    bsol=(best,wlist[0])
    bsol=CCheck(bsol)

    print(bsol[0],bsol[1])
    
### Start const####

# Pattern 1 #
#n=500
#count=400
#a=list(range(n))
##a=np.arange(n)
#print(a)
#iterations=1500
#mutproc=1/n#best choice
#mutchance=1 # best choice
#wproc=0.02
#gentransportation=0.01

def result():
    n=200
    count=160
    a=list(range(n))
    #a=np.arange(n)
    print(a)
    iterations=1000#1000
    mutproc=1/n#best choice
    mutchance=1 # best choice
    wproc=0.02
    CheckTimer=list(takewhile(lambda x : x< iterations, (i**2 for i in range(iterations))))
    print(CheckTimer)


    ### genPop ######
    pop=genPop(a,count)
    evolve(a,pop)

if __name__ == "__main__":    
    result()
    
    
            
                
            

    
        
    



