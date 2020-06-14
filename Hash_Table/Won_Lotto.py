def Won_Lotto(A,S):
    ## find sum of three numbers and store it in a set
    H=set()
    for i in range(len(A)):
        for j in range(i,len(A)):
            for k in range(j,len(A)):
                H.add((A[i]+A[j]+A[k],i,j,k))
    
    for i in range(len(A)):
        for j in range(i,len(A)):
            for k in range(j,len(A)):
                for x in H:
                    if x[0]== S-(A[i]+A[j]+A[k]):
                        return [A[x[1]], A[x[2]],A[x[3]], A[i],A[j],A[k]]
    return -1

A=[3,7,2,-1,-10]
Won_Lotto(A,21)

[3, 7, 2, 3, 3, 3]

