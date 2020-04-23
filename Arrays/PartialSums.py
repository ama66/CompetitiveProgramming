import numpy as np

def buildPartialSums(a):
    """O(N) precompute"""
    s=np.zeros(len(a))
    s[0]=a[0]
    for i in range(1,len(a)):
        s[i]=s[i-1]+a[i]
    return s

def Query(Left,Right):
    """O(1) lookup"""
    s=buildPartialSums(a)
    print(s)
    return s[Right] - s[Left - 1] if Left!=0 else  s[Right] 
    
    
a=np.random.randint(low = -10, high = 10, size = 15) 
print(a)

[ 3 -3  4  6 -7  5  6  1  4  7 -7 -1  5  4  5]
[ 3.  0.  4. 10.  3.  8. 14. 15. 19. 26. 19. 18. 23. 27. 32.]

5.0
