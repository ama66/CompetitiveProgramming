## Kill Monsters 

## If Monster damage is negative kill it! , throw all killed monsters in a priority queue and undo 
## the most damaging monsters if X (hp) falls below 0 by killing a monster, as long as there are potions available
import heapq

def Kill_Monsters_Greedy(D,K,x):
    H=[]
    count=0
    
    for elem in D:
        
        if elem <=0:
            x+=-elem
            count+=1
        else:
            x-=elem 
            heapq.heappush(H,-elem)
            count+=1
        
        while x <= 0 and K >0 and len(H)>0:
            x+=-1*(heapq.heappop(H))
            K-=1  
            
        if x <=0 and K<=0:
            return count
        
    return len(D) ## in case x is positive and I could kill all monsters

Damage=[-3,2,3,-2,8,8,6,4] # Monster Damage
Kpotion=2 # Number of Available potions
X=10 # Horse power/Health

Kill_Monsters_Greedy(Damage,Kpotion,X)       
8

