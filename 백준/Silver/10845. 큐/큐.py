from sys import stdin

queue = []

n = int(stdin.readline())

for i in range(n):
    x = stdin.readline().strip()
    
    if x[:4]=="push":
        queue.append(int(x[5:]))
    elif x=="pop":
        print(queue.pop(0)) if len(queue) else print(-1)
    elif x=="size":
        print(len(queue))
    elif x=="empty":
        print(0) if len(queue) else print(1)
    elif x=="front":
        print(queue[0]) if len(queue) else print(-1)
    else:
        print(queue[-1]) if len(queue) else print(-1)

    
