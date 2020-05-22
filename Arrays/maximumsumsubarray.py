def maxSubArraySum2(a,size): 
  
    max_sum = -math.inf ## a record of the maximum that will be compared to running sum and eventually returned
    max_ending_here = 0  ## move this pointer by 1 along the array and compare to sum seen so far from previous section of the array
    
    start = 0
    end = 0
    
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i] 
  
        if max_sum < max_ending_here: 
            max_sum = max_ending_here 
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
    
    return max_sum, start, end

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 

print("Maximum contiguous sum is", maxSubArraySum2(a,len(a)) )


a = [-2, -3, 4, -1, -2, 1, 5, -3] 

print("Maximum contiguous sum is", maxSubArraySum2(a,len(a)) )



Maximum contiguous sum is (-3, 1, 1)
Maximum contiguous sum is (7, 2, 6)

###############################################
## Dynamic Programming
def maxSubArraySumdp(a,size): 
      
    max_sum =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_sum = max(max_sum,curr_max) 
          
    return max_sum

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 

print("Maximum contiguous sum is", maxSubArraySumdp(a,len(a)) )

Maximum contiguous sum is -3


