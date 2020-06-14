
def Num_Pairs(A,s):
    Numpairs=0
    
    H={}
    
    for elem in A:
        
        if s-elem in H:  
            Numpairs+=H[s-elem]
            
        if elem not in H:
            H[elem]=1
        else:
            H[elem]+=1
        
    return  Numpairs

A=[3,-2,9,3,-2,4,9]

Su=7 

print(Num_Pairs(A,Su))

from collections import defaultdict

def Num_PairsDef(A,s):
    
    Numpairs=0
     
    H=defaultdict(int)
    
    for elem in A:
        
        if s-elem in H:
            
            Numpairs+=H[s-elem]
        
        H[elem]+=1
  
    return  Numpairs

A=[3,-2,9,3,-2,4,9]

Su=7 
Num_PairsDef(A,Su)
6
6
