## Largest Rectangle Area in a histogram. O(n) solutions involves fixing the index or height 
## and looking for two indices on the left and right with height smaller than the height at the current fixed index
## in this case maximum possible area with this height = height(index)*(Right-Left-1) 
## if I could not find index on the left we set it to -1 and if no one found on right we set it to n 
a=[6,2,5,4,5,1,6]
n=len(a)
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

a=[6,2,5,4,5,1,6]

Largest_Rect_Hist(a)


12
