# pigeon hole principle

def FindNumber(n):
    
    freq={}
    for i in range(1,n+1):
        freq[i]=0
        
    cur_rem=0 ## initialize 1111 numbers by 0 
    ## loop over all potential numbers 1, 11,111 ....up to n ones 
    for i in range(1,n+1):
        ## Generate potential candidate with "i" ones 
        cur_rem= (cur_rem * 10 + 1) % n
        if cur_rem==0: 
            print("Number found", "1"*i)
            return 
        else:
            if freq[cur_rem]!=0:
                print("Number found")
                print("1"*(i-freq[cur_rem])+"0"*freq[cur_rem])
                print("Formed from ", "1"*(i) , " And " , "1"*freq[cur_rem])
                return 
            else:
                freq[cur_rem]=i
                
    
n=15
FindNumber(n);

Number found
1110
Formed from  1111  And  1

# 74*15=1110
