from collections import deque

def solution(n, edge):
    adj = [[] for i in range(n+1)]
    visited = [0] * (n+1)
    
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    
    queue = deque([1])
    visited[1] = 1
    
    while queue:
        curr_node = queue.popleft()
        
        for next in adj[curr_node]:
            if not visited[next]:
                visited[next] = visited[curr_node] + 1
                queue.append(next)
    
    return visited.count(max(visited))