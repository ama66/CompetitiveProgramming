## find index of element ahead of current element that is larger than current element, for all elements
## of the array a , for last element will set it to -1 and also if no element is found greater than current
# will set anser to -1 
## put elements in stack in descending order. so push element to the stack, if you find next element greater
## than what is in the stack that must be the element we are looking for and we pop those elements from the
## stack that are smaller and update the index array with the index of this element that we are trying to
# push to the stack

def First_Greater_Element(a):
    ind_arr=[-1]*len(a)
    st=[] # I will store original element index in stack not the actual element itself
    for i in range(len(a)):
        while len(st)!=0 and a[st[-1]]<a[i]:
            ind_arr[st.pop()]=i
        st.append(i)
        
     
    return ind_arr
a=[2,4,5,1,10,0,9,12,15]
First_Greater_Element(a)

[1, 2, 4, 4, 7, 6, 7, 8, -1]
