N = int(input())


for i in range(N):
    stack = []
    parenthesis = input()

    for a in parenthesis:
        if a=='(':
            stack.append(a)
        elif a==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack):
            print('NO')
        else:
            print('YES')
        
                
    
