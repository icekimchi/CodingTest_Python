def solution(friends, gifts):
    gift = [ [0 for _ in range(len(friends))] for _ in range(len(friends))]
    n = []
    answer = [0 for i in range(len(friends))]
    
    for i, name in enumerate(gifts):
        send, receive = name.split(' ')
    
        for j in range(len(friends)):
            if send==friends[j]:
                index = friends.index(receive)
                gift[j][index] += 1
        
    for i in range(len(friends)):
        n_send = 0
        n_receive = 0
        for j in range(len(gift[i])):
            n_send += gift[i][j]
            n_receive +=  gift[j][i]
        n.append(n_send-n_receive)
        
    for i in range(len(gift)):
        for j in range(len(gift[i])):
            if i==j:
                continue
            a = gift[i][j]
            b = gift[j][i]
            if  a>b:
                answer[i] += 1
            elif a == b or (a==0 and b==0):
                if n[i] == n[j]:
                    continue
                else:
                    if n[i]>n[j]:
                        answer[i] += 1
    return max(answer)
            
