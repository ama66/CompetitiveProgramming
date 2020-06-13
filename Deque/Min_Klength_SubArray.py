# Minimum K-Length SubArray using deque:

def Min_KLength_SubArray(A,k):
    d=deque() # insert element in ascending order into the deque. Only insert index as a proxy for the element
    Ans=[] # put answer here
    for i in range(len(A)): 
        
        while len(d)!=0 and A[d[-1]]>=A[i]:
            d.pop()
        ## Now I am ready to insert element but before I do that let's make sure
        ## we popleft if d[0]=i-k
        if len(d)!=0 and d[0]==i-k:
            d.popleft()
        d.append(i) 
        
        if  i>=k-1:
            Ans.append(A[d[0]])
            
    return Ans

A=[-7,9,2,4,-1,5,6,7,1]
Min_KLength_SubArray(A,3)

[-7, 2, -1, -1, -1, 5, 1]
