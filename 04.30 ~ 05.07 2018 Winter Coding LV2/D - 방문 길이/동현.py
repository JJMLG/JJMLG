
def solution(dirs):
    answer = 0
    visited = []
    dir = {
        'U': 0,
        'L': 1,
        'R': 2,
        'D': 3,
    }
    direction = [[-1,0],[0,-1],[0,1],[1,0]]
    start = [5,5]
    
    for d in dirs:
        print(start)
        nx = start[0] + direction[dir[d]][0]
        ny = start[1] + direction[dir[d]][1]
        if 0 <= nx < 11 and 0 <= ny < 11:
            if [start[0],start[1],nx,ny] in visited or [nx,ny,start[0],start[1]] in visited:
                pass
            else:
                visited.append([start[0],start[1],nx,ny])
                answer += 1


            start[0] = nx
            start[1] = ny
            
            
        
    
    return answer