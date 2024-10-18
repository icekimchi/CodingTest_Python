from collections import defaultdict, deque

def DFS(graph, visited, v):
    visited[v] = 1
    print(v, end= " ")

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, visited, i)

def BFS(graph, visited, start):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        print(v, end= " ")
    
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

N, M, V = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

visited = [0] * (N+1)
DFS(graph, visited, V)
print()
BFS(graph, [0] * (N+1), V)
    
    
