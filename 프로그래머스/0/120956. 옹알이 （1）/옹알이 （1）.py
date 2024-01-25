def solution(babbling):
    babblings = ["aya", "ye", "woo", "ma"]
    temp = ""
    answer = 0
    
    for words in babbling:
        for i in range(len(words)):
            temp += words[i]
            if temp in babblings:
                temp = ""
        if len(temp)==0:
            answer += 1
        temp = ""          
    
    return answer