#### Z Traversal using Divide and Conquer
## assume you have a square with 2^n rows and 2^n columns fill it with numbers from 1 to 2^n 
## using z traversal. Divide into 4 half-sized squares of dimensions 2^(n-1) and 2^(n-1)
## until you get to a 4 1X1 squares where you fill top left (1) , top right (2) , lower left(3) and then lower 
## right (4) continue recursively..or go to square with n=0 this is 1X1 square, need to return 1 and add to
## cumulated answer
# find number at row x and column y
def Get_Val(n,x,y):
    #base case
    if n==0:
        return 1
    # if in upper half 
    if x <= (2**(n-1))-1:
        ## if in top left quadrant
        if y <= (2**(n-1))-1:
            return Get_Val(n-1,x,y)
        else: ## top right
            return (2**(2*n-2))+Get_Val(n-1,x, y-(2**(n-1)))
    else: ## lower half 
        if  y <= (2**(n-1))-1:
            return (2**(2*n-1)) + Get_Val(n-1,x-(2**(n-1)),y)
        else:
            return 3*(2**(2*n-2)) + Get_Val(n-1,x-(2**(n-1)),y-(2**(n-1)))
        
                                      
Get_Val(2,3,3)
16
