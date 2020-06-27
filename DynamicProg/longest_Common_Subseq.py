def longest_comm_subeq(A,B):
    n=len(A)
    m=len(B)
    dp=[[0 for e in range(m+1)] for e in range(n+1)]
    
    for i in range(1,n + 1): 
        for j in range(1,m + 1): 
            if A[i-1]==B[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    seq=[]
    return dp[n][m], reconstruct_lcs(dp,A,B,n,m,seq)

def reconstruct_lcs(dp,A,B,i,j,seq):
    if i<=0 or j<=0:
        return seq
    if A[i-1]==B[j-1]:
        reconstruct_lcs(dp,A,B,i-1,j-1,seq)
        seq.append(A[i-1])
        print(A[i-1])
    elif dp[i-1][j] > dp[i][j-1]:
        reconstruct_lcs(dp,A,B,i-1,j,seq)
    else:
        reconstruct_lcs(dp,A,B,i,j-1,seq)
    return seq
    
A=[1,7,1,8,3,6,5,9]
B=[7,3,9,8]
longest_comm_subeq(A,B)

7
3
9

(3, [7, 3, 9])


A = "AGGTAB"
B = "GXTXAYB"
print("Length of LCS is ", longest_comm_subeq(A, B)) 

G
T
A
B
Length of LCS is  (4, ['G', 'T', 'A', 'B'])


