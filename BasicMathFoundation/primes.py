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
    
        
        
