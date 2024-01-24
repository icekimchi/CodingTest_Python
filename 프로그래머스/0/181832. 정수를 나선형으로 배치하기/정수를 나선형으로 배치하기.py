def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    x = 0
    y = 0
    
    for i in range(n//2):
        x, y = i, i
        for j in range(n-1-2*i):
            answer[x][y] = count
            count += 1
            y += 1
        for j in range(n-1-2*i):
            answer[x][y] = count
            count += 1
            x += 1
        for j in range(n-1-2*i):
            answer[x][y] = count
            count += 1
            y -= 1
        for j in range(n-1-2*i):
            answer[x][y] = count
            count += 1
            x -= 1
    
    if (n%2!=0):
        answer[n//2][n//2] = count
    
    return (answer)

