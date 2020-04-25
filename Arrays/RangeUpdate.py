import numpy as np

a=np.array([-1,-2,2,1,3,4,5,6,8,11])
print("Original a ", a)

b=np.zeros(len(a))
s=np.zeros(len(a))


def Update(x,y,val):
    """build b array with multiple updates"""
    b[x]+=val
    b[y+1]-=val
    
def build_final_array():
    s[0]=b[0]
    a[0]+=s[0]
    
    for i in range(1,len(s)):
        s[i]=s[i-1]+b[i]
        a[i]+=s[i]

Update(3,5,2)
Update(3,5,-1)
build_final_array()
print("After Update a ", a)


Original a  [-1 -2  2  1  3  4  5  6  8 11]
After Update a  [-1 -2  2  2  4  5  5  6  8 11]
