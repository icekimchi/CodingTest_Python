def solution(wallet, bill):
    answer = 0
    target = min(wallet)
    
    while True:
        if max(bill)<=max(wallet) and min(bill)<=min(wallet):
            break
        else:
            bill[bill.index(max(bill))] //= 2
            answer += 1
            
            
    return answer