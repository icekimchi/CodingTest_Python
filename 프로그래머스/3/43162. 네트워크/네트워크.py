from collections import deque

def solution(n, computers):
    visited = [0] * n
    count = 0
    q = deque()
    
    while not all(visited):
        q.append(visited.index(0))
        print(q)
        
        while q:
            curr_node = q.popleft()
            visited[curr_node] = 1
            
            for i in range(n):
                if curr_node!=i and computers[curr_node][i]==1:
                    if not visited[i]:
                        visited[i] = 1
                        q.append(i)
        count += 1
        
    return count