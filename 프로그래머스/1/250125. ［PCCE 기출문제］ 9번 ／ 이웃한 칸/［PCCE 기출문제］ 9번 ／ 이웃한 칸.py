def solution(board, h, w):
    color = board[h][w]
    answer = 0
    
    for i in range(h-1, h+2):
        for j in range(w-1, w+2):
            if i<0 or i>=len(board):
                continue
            if j<0 or j==len(board):
                continue
            distance = abs(h-i) + abs(w-j)
            if distance==1:
                if color==board[i][j]:
                    answer += 1
    
    return answer