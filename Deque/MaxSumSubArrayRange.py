def maxSubArrayPsumRange(a,A,B): 
    ## Partial Sum Array
    s=[a[0]]
    for i in range(1,len(a)):
        s.append(s[i-1]+a[i])

    d=deque()
    ans=s[0]
    
    d.append(0)
    
    for Right in range(0,len(a)):
        
        ## any position before Right-B is not possible so pop it 
        if Right>B and len(d)!=0 and d[0]<Right-B:
            d.popleft()
           
        ## Minimum position to start looking for an answer is after A
        if (Right >=A):
            ans=max(ans,s[Right]-s[d[0]])
        
        ## Maintain ascending order so front is always the minimum 
        while len(d)!=0 and a[d[-1]]>=a[Right]:
            d.pop()
    
            
        d.append(Right)
        
    return ans

a = [100,-9,70,2,8,-1,1,50] 

maxSubArrayPsumRange(a,2,6)

130
