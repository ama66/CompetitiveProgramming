# Sieve of Eratosthenes optimized
import numpy as np


def Sieve_Erat(N):
    ## initialize array with True (all are prime unless we invalidate this later!)
    for i in range(2,N+1):
        IsPrime[i]=1
    
    for i in range(2,int((N+1)/2)):
        if is_prime(i):
            for j in range(2*i, N+1, i ):
                 IsPrime[j]=0
        

N=20
IsPrime=np.zeros(N+1)
Sieve_Erat(N)

for i in range(N+1):
    if IsPrime[i]:
        print(i)
        
2 3 5 7 11 13 17 19
