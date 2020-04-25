a=np.array([7,3,4,5,5,6,7,3])
Freq=np.zeros_like(a)

def Freq_Arr():
    cnt=0
    for elem in a:
        if Freq[elem]==0:
            cnt+=1
        Freq[elem]+=1
    return cnt 
print(a)
print(Freq_Arr())
print(Freq)


[7 3 4 5 5 6 7 3]
5
[0 0 0 2 1 2 1 2]
