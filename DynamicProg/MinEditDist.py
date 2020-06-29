# DP 
def MinEditDistDP(str1, str2, m, n): 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0: 
                dp[i][j] = j    
            elif j == 0: 
                dp[i][j] = i     
  
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
    seq=[]

    return dp[m][n] , reconstruct_edits(dp,str1,str2,m,n,seq)

def reconstruct_edits(dp,str1,str2,i,j,seq):
    
    if i==0:
        if j!=0:
            seq.append((str2[0:j],"Insert"))
        return seq
    
    if j==0:
        if i!=0:
            seq.append((str1[0:i],"Remove"))
        return seq
        
    if str1[i-1]==str2[j-1]:
        reconstruct_edits(dp,str1,str2,i-1,j-1,seq)
        seq.append((str1[i-1],"Do Nothing"))
    else:
        minim=(0,-1)
        for inc in [(-1,-1),(-1,0)]:
            if dp[inc[0]+i][inc[1]+j] < dp[minim[0]+i][minim[1]+j]:
                minim=inc
        if minim==(0,-1):
            reconstruct_edits(dp,str1,str2,i,j-1,seq)
            seq.append((str2[j-1],"Insert"))
        elif minim==(-1,-1):
            reconstruct_edits(dp,str1,str2,i-1,j-1,seq)  
            seq.append(((str1[i-1],str2[j-1]),"Replace"))
        elif minim==(-1,0):
            reconstruct_edits(dp,str1,str2,i-1,j,seq)
            seq.append((str1[i-1],"Remove"))
       
    return seq
    
    
    

str1 = "sunday"
str2 = "saturday"
m=len(str1)
n=len(str2)

MinEditDistDP(str1,str2,m,n)

(3,
 [('s', 'Do Nothing'),
  ('a', 'Insert'),
  ('t', 'Insert'),
  ('u', 'Do Nothing'),
  (('n', 'r'), 'Replace'),
  ('d', 'Do Nothing'),
  ('a', 'Do Nothing'),
  ('y', 'Do Nothing')])
  
  str1 = "abx"
str2 = "a"
n=len(str1)
m=len(str2)


MinEditDistDP(str1,str2,n,m)

(2, [('a', 'Do Nothing'), ('b', 'Remove'), ('x', 'Remove')])


