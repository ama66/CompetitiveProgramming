from collections import defaultdict

def LongestCommonSubseq(a):
    #fix left and then iterate over right and keep a record of max and min seen between left and right
    # ensure you have distinct numbers between left and right using frequency array or hashmap 
    # ensure maxe - mine within the subsequence = Right - left 
    maxlen=0
    
    for left in range(len(a)):
        # Reset hashmap
        freq=defaultdict(int)
        mine=maxe=a[left]
        
        for right in range(left,len(a)):
            mine=min(mine,a[right])
            maxe=max(maxe,a[right])
            
            if freq[a[right]]!=0:
                break
            else:
                freq[a[right]]=1
            
            if maxe-mine==right-left:
                maxlen=max(maxlen,right-left+1)
                
    return maxlen

a=[1,2,3,3,5,6,4]   
            
print(LongestCommonSubseq(a))


a=[1,1,3,2,5,6,4]   

print(LongestCommonSubseq(a))


4
6
