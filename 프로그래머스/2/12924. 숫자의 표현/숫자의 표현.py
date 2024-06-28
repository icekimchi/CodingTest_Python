def solution(n):
    if n==1:
        return 1
    answer = 1
    
    for i in range(1, n):
        sum = 0 
        for j in range(i, n):
            sum += j
            if sum==n:
                answer += 1
            elif sum>n:
                break
                
    return answer