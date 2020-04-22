## Prime Factorization 
import math
#Fast Modular Exponentiation  
## A^2 mod C = (A * A) mod C = ((A mod C) * (A mod C)) mod C
## also (A^2)^ n mod c = (A^2 mod c)^ n  mod c 
## pow(pow(a, 2),31) % mod = pow(pow(a , 2) % mod , 31) % mod 
a=6
n=2
mod=10

print("regular expo:", pow(a, n) % mod )
def fast_exp_rec(a,n,mod):
    if n==0:
        return 1 
    if n % 2 == 0 :
        return fast_exp_rec((a*a) % mod , n/2 , mod)
    return a % mod *fast_exp_rec(a , n-1 , mod) % mod 
        
    
def fast_exp_it(a,n,mod):
    ans=1
    while n>=1:
        if (n%2==0):
            a =(a*a) % mod
            n=n/2
            print("Even" , a , n , ans)
        else:
            ans=ans*a 
            n=n-1
            print("Odd" , a , n , ans)

    return ans 
print("Recursive ", fast_exp_rec(a,n,mod))
print("Itertive ", fast_exp_it(a,n,mod))

regular expo: 6
Recursive  6
Even 6 1.0 1
Odd 6 0.0 6
Itertive  6
