## Prime Factorization 
import math

def is_prime(n):
    """O(sqrt(n)) implementation"""
    
    if n <=1: 
        return False
    else:
        i=2
        while (i <=math.sqrt(n)):
            if n % i==0:
                return False
            i+=1
            
        return True
    
        
        
## Prime Factorization 
import math

def prime_fac(n):
    """O(sqrt(n)) implementation"""
    Factors={} ## key=factor, value=exponent
    # Start with the minimum possible factor = 2
    d=2
    while n > 1: 
        # for a given factor d find exponent/how many times n can be divided by this factor 
        k=0
        while n%d==0: 
            n/=d
            k+=1
        ## if I have a prime factor d find exponent update hashtable
        if k > 0:
            Factors[d]= k 
        d+=1
    ## If I exist the while and n > 1 it means there are no more factors
    if n > 1:
        Factors[n]=1
    return Factors
    
    
            
prime_fac(26)

#{2: 1, 13: 1}
            
        
    
        
        

