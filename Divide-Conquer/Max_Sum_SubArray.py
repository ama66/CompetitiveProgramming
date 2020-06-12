
def Max_Sum_SubArr_DivQ(a,left,right):
    ## we will use divide and conquer to solve this problem through merge sort
    if left==right:
        return a[left]
    
    mid= (left+right) //2 
    
    ans=max(Max_Sum_SubArr_DivQ(a,left,mid), Max_Sum_SubArr_DivQ(a,mid+1,right))
    
    leftsum=max_left_sum(a,left,mid)
    rightsum=max_right_sum(a,mid,right)
    
    
    return max(ans,leftsum+rightsum)

def max_left_sum(a,left,mid):
    sum=0
    maxsum=a[mid]
    for i in range(mid,-1,-1):
        sum=sum+a[i]
        maxsum=max(maxsum,sum )
    return maxsum 

def max_right_sum(a, mid , right ):
    sum=0
    maxsum=a[mid+1]
    for i in range(mid+1,right+1):
        sum=sum+a[i]
        maxsum=max(maxsum,sum )
    return maxsum 


    
a=[-1,2,3,4,-1,6,-5]  
left=0
right=len(a)-1
      
Max_Sum_SubArr_DivQ(a,left,right) 

14
