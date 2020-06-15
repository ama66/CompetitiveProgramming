def Act_Sel(A):
    ## sort in ascending end time. Pick those classes that end first 
    A.sort(key = lambda x: x[1])
    count=0
    cur_finish=-1
    List_Act=[]
    for start,finish in A:
        if cur_finish < start:
            count+=1
            cur_finish=finish
            List_Act.append((start,finish))
            
    return count,List_Act
A=[(1,4),(3,5),(0,6),(5,7),(3,8),(5,9),(6,10),(8,11),(8,12),(2,13),(12,14)]
Act_Sel(A)

(4, [(1, 4), (5, 7), (8, 11), (12, 14)])

