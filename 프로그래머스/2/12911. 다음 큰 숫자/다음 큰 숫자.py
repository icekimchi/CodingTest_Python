def solution(n):
    target = n
    countN = bin(n)[2:].count("1")
    
    while True:
        target += 1
        if bin(target)[2:].count("1") == countN:
            return target
    

