
# Shortest path in a Maze

from collections import deque

dir_vec=[(0,-1),(0,1),(-1,0),(1,0)]

def isValid(mat, visited, row, col):
    
    loc_check= row >=0 and row < N and col >=0 and col < M
    if loc_check==False:
        return False
    
    visit_check= visited[row][col]==False
    is_free =mat[row][col] == 1 
    
    return visit_check and is_free



# Find Shortest Possible Route in a matrix mat from source
# cell (i, j) to destination cell (x, y)

def BFS(mat, i, j, x, y):
    
    if (x > N or y > M):
        print("Error: Point is outside the maze boundaries")
        return 
        
    visited = [[False for y in range(M)] for x in range(N)]
    q = deque()
    visited[i][j] = True
    
    ## initialize distance (third parameter) to zero at the root cell. Every time you append a new cell 
    ## on the new search "front" add 1 to the distance 
    q.append((i, j, 0))
    min_dist = float('inf')

    while q:
        
        (i, j, dist) = q.popleft()
        
        ##BFS will give you the shortest distance if we end up at the required cell position
        if i == x and j == y:
            min_dist = dist
            break

        for row,col  in dir_vec:
            # check if it is possible to go to the required position
            # by visiting neighbors 
            if isValid(mat, visited, i + row, j + col):
                # mark next cell as visited and enqueue it
                visited[i + row][j + col] = True
                q.append((i + row, j + col, dist + 1))

    if min_dist != float('inf'):
        print("The shortest path from source to destination has length", min_dist)
    else:
        print("Destination can't be reached from given source")


if __name__ == '__main__':

    # input maze
    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]

    # M x N matrix
    M = N = 10

    # Find shortest path from source (0, 0) to destination (7, 5)
    BFS(mat, 0, 0, 7, 5)
    
  The shortest path from source to destination has length 12
  
  BFS(mat, 0, 0, 7, 15)
  
  Error: Point is outside the maze boundaries
    
