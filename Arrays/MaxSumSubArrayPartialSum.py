## Using Partial Sums
def maxSubArrayPsum(a,size): 
    ##Build Partial Sums
    s=[a[0]]
    for i in range(1,size):
        s.append(s[i-1]+a[i])
        
    mins=0 ## initial value for minimum sum seen so far
    maxsum=a[0]
    
    for i in range(0,size):
        maxsum=max(maxsum, s[i]-mins)
        #update min sum seen so far
        if s[i]< mins:
            mins=s[i]
    
    
    return maxsum
    
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 

print("Maximum contiguous sum is", maxSubArrayPsum(a,len(a)) )

a = [-2, -3, 4, -1, -2, 1, 5, -3] 

print("Maximum contiguous sum is", maxSubArrayPsum(a,len(a)) )


Maximum contiguous sum is -3
Maximum contiguous sum is 7
