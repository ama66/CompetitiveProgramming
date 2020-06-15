## Given upper left corner l1,c1 indices and lower right corner l2,c2 compute sum of submatrix defined by these
## Corners
def Partial_Sums(Mat,l1,c1,l2,c2):
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
            
    return PartialSums[l2][c2]-PartialSums[l1-1][c2]-PartialSums[l2][c1-1]+PartialSums[l1-1][c1-1]

    
M=[[1,2 ,3 ,6],
   [5,6, -1,8],
   [6,0, 1,3 ],
   [8,9,10,-6]]

            
print(Partial_Sums(M,1,1,3,2))
25
