from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    #상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(0, 0)])
    visited = [ [0]*m for _ in range(n) ]
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m or \
                maps[nx][ny]==0:
                continue
                
            if not visited[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                visited[nx][ny] = 1
    
    for i in range(n):
        for j in range(m):
            print(maps[i][j], end="")
        print()
    
    return maps[n-1][m-1] if maps[n-1][m-1]>1 else -1
                
                
                
                
                
                
        
        
    
    
        
        
