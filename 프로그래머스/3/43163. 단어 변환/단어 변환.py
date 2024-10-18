from collections import deque
    
def solution(begin, target, words):
    q = deque([(begin, 0)])
    visited = {}
    depth = 0
    
    for x in words:
        visited[x] = 0
    
    if target not in words:
        return 0
    
    while q:
        temp, depth = q.popleft()
        print(temp, depth)
        
        if temp==target:
            return depth
        
        for i, word in enumerate(visited):
            if not visited[word]: #확인 안 한 단어라면
                cnt = 0
                for i in range(len(word)):
                    if temp[i]!=word[i]:
                        cnt += 1
                        
                if cnt==1:
                    q.append([word, depth+1])
    return answer
            