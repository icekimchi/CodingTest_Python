def solution(lines):
    answer = 0
    
    sets = [set(range(min(line), max(line))) for line in lines]
    
    answer = sets[0] & sets[1] | sets[0]&sets[2] | sets[1]&sets[2]
    
    return len(answer)