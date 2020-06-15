import heapq

def Connect_Ropes(H):
    pq=[]
    for elem in H:
        heapq.heappush(pq,elem)
    cost=0
    while len(pq)!=1:
        min1=heapq.heappop(pq)
        min2=heapq.heappop(pq)
        cost+=min1+min2
        heapq.heappush(pq,min1+min2)
        
    return cost 

H=[4,3,2,6]
Connect_Ropes(H)
29 

