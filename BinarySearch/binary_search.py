## Minimum capacity transportation

## what is the minimum capacity truck to transport boxes (weights given by g) in order from left to right
## in maximum k trips 

def MinCapTransport(g,n,k):
    ## solve by searching capacities in binary search fashion
    Min_Cap=max(g)
    Max_Cap=sum(g)
    Left=Min_Cap
    Right=Max_Cap
    
    while Left <= Right:
        ## Find how many trips for halfway capacity
        Middle=Left + (Right-Left)//2
        Numtrips=FindTrips(Middle,g)
        
        if Numtrips > k: 
            ## capcity is not sufficient so need to search the right half 
            Left=Middle+1
        else:
            ## I have an answer but could improve on it potentially by searching lower capacities
            ans=Middle
            Right=Middle-1
            
    
    return ans

def FindTrips(cap,g):
    
    sumcap=0
    trips=1
    for elem in g:
        if sumcap+elem <= cap:
            sumcap+=elem
        else:
            trips+=1
            sumcap=elem
            
    return trips


    
g=[7,3,2,3,1,4]
n=len(g)
k=3
MinCapTransport(g,n,k)
8


g=[2,3,4]
n=len(g)
k=2
MinCapTransport(g,n,k)
5


