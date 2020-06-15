def MaxSizeSquare(M):
#     /// maxLen[i][j] = max. x such as (i - x + 1, j - x + 1) -->
#                                 /// (i, j) full of 1s
#                                 /// maxLen[i][j] = min(maxLen[i-1][j], maxLen[i][j-1],
#                                                     /// maxLen[i-1][j-1]) + 1, a[i][j] = 1.
#                                                     /// = 0, otherwise

    n=len(M)
    m=len(M[0])
    maxLen=[[0 for j in range(m)] for i in range(n)]
    ans=0
    for i in range(1,n):
        for j in range(m):
            if M[i][j]==0:
                maxLen[i][j]=0
            else:
                maxLen[i][j] = min(maxLen[i - 1][j], maxLen[i][j - 1], maxLen[i - 1][j - 1] ) + 1

            ans = max(ans, maxLen[i][j])

    return ans 
M=[[0,1,0,0,1],
   [1,0,1,1,1],
   [1,1,1,1,1],
   [1,1,1,1,1],
   [0,1,0,1,0]]

MaxSizeSquare(M)

3

