def maxSubArray(a): 
    size=len(a)
    maxsum=a[0]
    cursum=0
    for i in range(size):
        cursum+=a[i]
        maxsum=max(maxsum, cursum)
        if cursum < 0:
            cursum=0
            
    return maxsum


def MaxSumSubMatrix(M):
    ## Define Partial Sums SubArray defined as UpSum[i][j] = a[1][j] + a[2][j] + ... + a[i][j]
    n=len(M)
    m=len(M[0])
    UpSum=[[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0:
                UpSum[0][j]=M[0][j]
            else:
                UpSum[i][j]= UpSum[i-1][j]+M[i][j]
    
    ## Now we will fix r1 and r2 and compute column sum between r1 and r2 defined as
    ##  v[j] = a[r1][j] + a[r1+1][j] + ... + a[r2][j]
    v=[0 for j in range(m)]
    ans=-1e8
    for r1 in range(n):
        for r2 in range(r1,n):
            for j in range(1,m):
                if r1==0:
                    v[j]=UpSum[r2][j]
                else:  
                    v[j]=UpSum[r2][j]-UpSum[r1-1][j]
            ans = max(ans, maxSubArray(v))   
    return ans

M=[[1 ,  2, -1, -4, -20],
   [-8, -3, 4 , 2,  1],
   [3 , 8 , 10, 1 , 3],
   [-4,-1 , 1 , 7, -6]]
MaxSumSubMatrix(M)
29

