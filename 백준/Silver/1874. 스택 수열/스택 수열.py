import sys
n = int(sys.stdin.readline())

def solution(n):
    stack = []
    ans = ""
    cur = 1
    for _ in range(n):
        x = int(sys.stdin.readline().strip())
        
        while cur<=x:
            stack.append(cur)
            cur += 1
            ans += "+"
            
        if stack[-1]==x:
            stack.pop()
            ans += "-"
        else:
            return "NO"
    return ans
        
ans = solution(n)
if ans=="NO":
    print(ans)
else:
    for i in ans:
        print(i)
