# Flood Algorithm
## A group of connected 1s forms an island.
## Define Global variables that get passed along in the recursion (pointer reference)

def is_valid(i,j):
    loc_check= i>=0 and i < nrow and j>=0 and j < ncol
    if loc_check==False:
        return False
    visit_check= visited[i][j]==False
    is_island=graph[i][j]==1
    return visit_check and is_island

def fill_graph(idx,jdx):
    global cellcnt 
    visited[idx][jdx]=True 
    cellcnt+=1 
    for i_inc, j_inc in dir_vec:       
        if is_valid(idx+i_inc,jdx+j_inc):
            fill_graph(idx+i_inc,jdx+j_inc)

        
dir_vec=[(0,-1),(0,1),(-1,0),(1,0)]
graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]]   
  
nrow = len(graph) 
ncol = len(graph[0]) 
visited=[[False for j in range(ncol)] for j in range(nrow)]
num_islands=0 
max_cell_cnt=0

for i in range(nrow):
    for j in range(ncol):
        if is_valid(i,j):
            cellcnt=0
            fill_graph(i,j)
            num_islands+=1
            max_cell_cnt=max(max_cell_cnt,cellcnt)
            
print("Num of Islands= ", num_islands)
print("Max cell count in an island = ", max_cell_cnt)

6
3
