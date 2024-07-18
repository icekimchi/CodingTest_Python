def bomb(board, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            a = max(0, min(x+i, len(board)-1))
            b = max(0, min(y+j, len(board)-1))
            if board[a][b] == 0:
                board[a][b] = 2
            
    return board
        
def show(board):
    for line in board:
        print(line, end="\n")
    print("\n")
        
            

def solution(board):
    answer = 0
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] ==1:
                board = bomb(board, x, y)
                show(board)
                
    for line in board:
        answer += line.count(0)
            
    return answer
    
    