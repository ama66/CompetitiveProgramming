# Max size Rectangle out of a 2D array of 0 and 1. This problem can be solved if we fix lower row r2 
## and consider all potential rectangles formed above this row. For a given row this problem is identical
## to max area in a histogram where histogram heights is formed by heights above this row. To get such heights
## we add ones all the way until a 0 is hit. if we start from 0 the height=0. We will precompute the histogram 
## heights for all rows. Finally we will pick max area amongst all of those areas computed for all possible r2's 
def First_Smaller_Right(a):
    ## put elements in the stack in ascending(small to large)
    ind_arr=[len(a)]*len(a)
    st=[] # I will store original element index in stack not the actual element itself
    for i in range(len(a)):
        while len(st)!=0 and a[st[-1]] > a[i]:
            ind_arr[st.pop()]=i
        st.append(i)
    return ind_arr

def First_Smaller_Left(a):
    ## put elements in the stack in ascending(small to large)
    ind_arr=[-1]*len(a)
    st=[] # I will store original element index in stack not the actual element itself
    for i in range(len(a)-1,-1,-1):
        while len(st)!=0 and a[st[-1]] > a[i]:
            ind_arr[st.pop()]=i
        st.append(i)
    return ind_arr


def Largest_Rect_Hist(a):
    ## First will find smaller element on left and right using algorithm similar
    ## to the next greater element but starting once from index 0 and moving to the right
    # and starting at n-1 and moving to the left 
    Left_Arr=First_Smaller_Left(a)
    Right_Arr=First_Smaller_Right(a)
    Max_Area=-1
    for k in range(len(a)):
         Max_Area=max( Max_Area, a[k]*(Right_Arr[k]-Left_Arr[k]-1))
            
    return Max_Area


def Largest_Rectangle_2D(A):
    ## First precompute tower/histogram heights for all rows
    nrows=len(A)
    ncols=len(A[0])
    Tower=[[0 for j in range(ncols)] for i in range(nrows)]
    Tower[0][:]=A[0][:]
    for r in range(1,nrows):
        for c in range(ncols):
            if A[r][c]==0:
                Tower[r][c]=0
            else:
                Tower[r][c]=Tower[r-1][c]+1 
    max_area=-1
    for r in range(nrows):
        max_area=max(max_area,  Largest_Rect_Hist(Tower[r][:]))
    return max_area

A=[[1,1,0,1,1,0,1],
   [1,1,1,0,1,1,1],
   [1,1,1,1,1,1,1],
   [0,1,1,1,1,0,1]]

Largest_Rectangle_2D(A)
    
  8
  
