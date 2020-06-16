## Student list with weights list w[], number N, can get on a boat. Boat capacity is Wmax 
## 2 students max can get on a boat. Difference between student weights should nopt exceed B 
## What is min number of boats to cross the river?
def MinNoBoats(N,W,Wmax,B):
    p=0
    Minboats=0
    n=len(W)
    W.sort()
    IsTaken=[False for st in W]
    H=[]
    for i in reversed(range(n)):
        while p < i and  W[i]+W[p]<=Wmax : 
            ## push to the queue elements statisfyinf first requirement
            heapq.heappush(H,(-W[p],p))
            p+=1
        ## cur student could have been paired with previous student so need to check 
        if IsTaken[i]:
            continue 
        ## Now look for a pair to satisfy the second requirement. 
        while len(H)>0 and W[i]-(-1*(H[0][0]))<=B: 
        ## that could be a potential pair but need to check to make sure it is not taken
            if IsTaken[H[0][1]] or H[0][1]==i:
                heapq.heappop(H)
            else:
                IsTaken[i]=IsTaken[H[0][1]]=True
        ## Whether I find a match or not need to increase number of boats
        Minboats+=1
  
    return Minboats
                               
W=[81,37,32,88,55,93,45,72]
N=8
Wmax=100
B=10
MinNoBoats(N,W,Wmax,B)         
6
