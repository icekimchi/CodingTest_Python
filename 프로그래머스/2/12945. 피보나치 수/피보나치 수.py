
def solution(n):
    n0 = 0
    n1 = 1
    
    for i in range(n-1):
        n2 = n0 + n1
        
        if n==2:
            return (n0+n1)%1234567
        
        n0 = n1
        n1 = n2
    
    return n2%1234567
    
    