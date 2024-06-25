def del_0(a):
    cnt = 0
    new = ""
    for s in a:
        if s=="1":
            new += "1"
            continue
        cnt += 1
    
    return cnt, new

    
def solution(s):
    ans_0 = 0
    new_s = ""
    ans = 0
    
    while s!="1":
        tmp_0, new_s = del_0(s)
        s = bin(len(new_s))[2:]
        print(s)
        
        
        ans_0 += tmp_0
        ans += 1
    
    return [ans, ans_0]
