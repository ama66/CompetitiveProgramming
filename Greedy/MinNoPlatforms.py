class TransitEvent:
    def __init__(self,time,typeofevent):
        self.time=time
        self.eventtype=typeofevent
        
    def __gt__(self, other):
        if not isinstance(other, TransitEvent):
            return NotImplemented
        return self.time > other.time
    
class EventList:
    def __init__(self):
        self.eventlist=[]
        
    def build_eventlist(self,ArrArray,DepArray):
        for TEvent in ArrArray:
            self.eventlist.append(TransitEvent(TEvent,"Arrival"))
        for TEvent in DepArray:
            self.eventlist.append(TransitEvent(TEvent,"Departure"))
            
    def MinPlatforms(self):
        self.eventlist.sort()
        
        Curr_Req_Platforms=0 
        Min_Platforms=0
        
        for i in range(len(self.eventlist)):
            if self.eventlist[i].eventtype=="Departure":
                Curr_Req_Platforms-=1
            else:
                Curr_Req_Platforms+=1
                
            Min_Platforms=max(Min_Platforms,Curr_Req_Platforms)
            
        return Min_Platforms
        
        
Arr=[900, 940, 950, 1100, 1500, 1800]
Dept=[910, 1200, 1120, 1130, 1900, 2000]
E=EventList()
E.build_eventlist(Arr,Dept)
E.MinPlatforms()
3
