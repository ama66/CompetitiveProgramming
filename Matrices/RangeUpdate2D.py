## Range Update Trick
def Build_Partial_Sums(Mat):
    ## First Do construct sum centered at l2,c2 (lower right corner)
    nrows=len(Mat)
    ncols=len(Mat[0])
    PartialSums=[[0 for j in range(ncols)] for i in range(nrows)]
    ## First Construct sum 
    #Compute First Row and then first column
    PartialSums[0][0]=Mat[0][0]
    for j in range(ncols):
         PartialSums[0][j]=PartialSums[0][j-1]+Mat[0][j]
    for i in range(1,nrows):
         PartialSums[i][0]=PartialSums[i-1][0]+Mat[i][0]
    ## Now use Recurrence Relation safely
    for i in range(1,nrows):
        for j in range(1,ncols):
            PartialSums[i][j]=PartialSums[i][j-1]+PartialSums[i-1][j]+Mat[i][j]-PartialSums[i-1][j-1]
    return PartialSums

## Now update range from (upper left corner point) r1,c1 to (lower right corner point) r2,c2 with value val

def UpdateRange(A,r1,c1,r2,c2,val):
    nrows=len(A)
    ncols=len(A[0])
    B=[[0 for j in range(ncols)] for i in range(nrows)]
    B[r1][c1]+=val
    B[r1][c2+1]-=val
    B[r2+1][c1]-=val
    B[r2+1][c2+1]+=val
    
    PS=Build_Partial_Sums(B)
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            A[i][j]+=PS[i][j]
    
    return A 

M=[[1,2 ,3 ,6],
   [5,6, -1,8],
   [6,0, 1,3 ],
   [8,9,10,-6]]

UpdateRange(M,0,0,2,2,5)

[[6,   7, 8,  6], 
 [10, 11, 4, 8], 
 [11, 5,  6, 3], 
 [8, 9,  10, -6]]


