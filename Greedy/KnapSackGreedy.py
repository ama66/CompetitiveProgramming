class KnapsackItem:
    def __init__(self,w,v):
        self.w=w
        self.v=v
        self.vpu=float(self.v)/float(self.w)
    def __gt__(self, other):
        if not isinstance(other, KnapsackItem):
            return NotImplemented
        return self.vpu > other.vpu
    
class KnapSack:
    def __init__(self,G):
        self.itemlist=[]
        self.remaining_capacity=G
        self.capacity=G
        self.final_bag=[]
        self.n=0
        
    def Build_KnapSack(self,w_arr,v_arr):
        for i in range(len(w_arr)):
            self.itemlist.append(KnapsackItem(w_arr[i],v_arr[i]))
        self.n=len(w_arr)
        
    def _Sort_By_Vpu(self):
        self.itemlist=sorted(self.itemlist,reverse=True)
    def Fill_KnapSack(self):
        self._Sort_By_Vpu()
        MaxCap=0
        for i in range(self.n):
            curr_weight=self.itemlist[i].w
            curr_val=self.itemlist[i].v
            ## check if I can insert it fully into the knapsack
            if self.remaining_capacity - curr_weight >=0:
                self.remaining_capacity-=curr_weight
                MaxCap+=curr_val
                self.final_bag.append(("wt: "+str(self.itemlist[i].w) ,"value: "+str(self.itemlist[i].v),"fraction: "+str(1)))
            else: # Check if I can take a fraction
                frac=self.remaining_capacity/curr_weight
                MaxCap+=curr_val*frac
                self.remaining_capacity-=frac*curr_weight
                self.final_bag.append(("wt: "+str(self.itemlist[i].w) ,"value: "+str(self.itemlist[i].v),"fraction: "+str(frac)))

                break
                
        return MaxCap
    
        

w=[2,3,5,7,1,4,1]
v=[10,5,15,7,6,18,3]
G=10

# KS=KnapSack(1)
# KS.Build_KnapSack(w,v)
# KS.itemlist.sort(reverse=True)
# [KS.itemlist[i].v for i in range(len(w))]
# #KS.Fill_KnapSack()
# [KS.itemlist[i].w for i in range(len(w))]
#[KS.itemlist[i].w for i in range(len(w))]


KS=KnapSack(10)
KS.Build_KnapSack(w,v)
KS.Fill_KnapSack()
43.0

KS.final_bag
[('wt: 1', 'value: 6', 'fraction: 1'),
 ('wt: 2', 'value: 10', 'fraction: 1'),
 ('wt: 4', 'value: 18', 'fraction: 1'),
 ('wt: 5', 'value: 15', 'fraction: 0.6')]

