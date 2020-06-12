## given a list of point coords [(x1,y1),(x2,y2)....etc] find maximum of all special distances between points.
## to answer this it is efficient to first sort the points based on x coordinate. then for a given point xj 
## look back at ponts with smaller xi so xj-xi will be greater than a distance D for a set of points
## starting at some index i all the way to certain p this condition will be satisfied along with
## yj-yi > Distance which is required for min(|xj-xi|,|yj-yi|) >= Distance to hold.
## note that for this condition to hold both |xj-xi|> = Distance and |yj-yi|>=Dist
def Max_Special_Dist(n, a):
    # use binary search
    x=-1e6 ## Answer we are looking for
    left=0
    right=1e6
    ## sort based on x coordinate (first number in the tuple)
    a.sort(key= lambda x: x[0])

    while left <= right:
        mid=int((left + right)//2)
        if Is_Valid_Dist(mid,a):
            x=mid
            left=mid+1
        else:
            right=mid-1
    return x

def Is_Valid_Dist(Dist,a):
    n=len(a)
    p=-1
    miny=1e3
    maxy=-1e3
    for j in range(0,n):
        while p+1 < j and a[j][0] - a[p+1][0] >=Dist:
            p+=1
            miny=min(miny, a[p][1])
            maxy=max(maxy, a[p][1])
        if p!=-1 and abs(miny - a[j][1]) >=Dist:
            return True 
        if p!=-1 and abs(maxy - a[j][1]) >=Dist:
            return True 
    return False 

a=[(1, 3),(2 , 1),(3 , 2) , (5 , 4) , (4, 0)]

Max_Special_Dist(len(a), a)

3
