## Given frequency array a containing for each index how many available animals 
## find max no of groups of distinct k animals that can be formed out of all animals 
# use binary search. Maximum number of groups is sum(a)/k  if for a given number of groups x
## you sum for each element in [a] the minimum of the number min(a[i],x) if the sum > x*k then
## this is possible otherwise it is not possible to form this number of groups of distinct k animals 
## for a=[8,6] maximum number of groups of distinct 2 animals is obviously 6 (good test case!)

def Max_No_Groups(a , n, k ):
    # use binary search
    x=0
    left=0
    right=sum(a)/k
    
    while left <= right:
        mid=int((left + right)//2)
        if isValid(a,n,k,mid):
            x=mid
            left=mid+1
        else:
            right=mid-1
    return x

def isValid(a , n ,  k , x ):
    sum=0
    for elem in a:
        sum+=min(elem, x)
    return sum >= x*k

a=[8,6]
n=len(a)
k=2

Max_No_Groups(a , n, k )
6

a=[8, 3, 5]
n=len(a)
k=2
Max_No_Groups(a , n, k )

8

    
