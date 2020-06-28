def knapSack(Wmax, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    for i in range(1,n + 1): 
        for w in range(1,Wmax + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    seq=[]
    return K[n][Wmax] , reconstruct_knapSack(K,wt,n,Wmax,seq,Rem_Cap=Wmax)

def reconstruct_knapSack(K,wt, i,j , seq,Rem_Cap):
    if i<=0 or j<=0 or Rem_Cap <=0:
        return seq
    
    if K[i][j] == K[i-1][j]:
        reconstruct_knapSack(K,wt, i-1,j , seq , Rem_Cap )
    else:
        seq.append(wt[i-1])
        Rem_Cap-=wt[i-1]
        reconstruct_knapSack(K,wt, i-1,j , seq , Rem_Cap )
        
    return seq
            
        
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 


(220, [30, 20])


