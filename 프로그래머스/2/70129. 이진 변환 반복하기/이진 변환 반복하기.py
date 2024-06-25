def solution(s):
    cnt_0 = 0
    ans = 0
    
    while s!="1":
        cnt_0 += s.count('0')
        s = str(len(s) - s.count('0'))
        s = bin(int(s))[2:]
        ans += 1
    
    return [ans, cnt_0]
