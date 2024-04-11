import sys

n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

N.sort()

for m in M:
    start = 0
    end = n-1
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if m==N[mid]:
            ans = 1
            break
        elif m>N[mid]:
            start = mid+1
        elif m<N[mid]:
            end = mid-1
    print(ans)
        
        
    
    
    
