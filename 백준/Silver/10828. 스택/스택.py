import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    x = sys.stdin.readline().strip()

    if x[:4]=="push":
        x, n = x.split()
        stack.append(n)
    elif x=="pop":
        if len(stack)>0:
            print(stack.pop())
        else:
            print(-1)
    elif x=="size":
        print(len(stack))
    elif x=="empty":
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif x=="top":
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
    
