def getslope(d1, d2):
    return (d1[0]-d2[0]) / (d1[1]-d2[1])
        

def solution(dots):
    answer = 0
    d_length = 4
    
    slope1_1 = getslope(dots[0], dots[1])
    slope1_2 = getslope(dots[2], dots[3])
    slope2_1 = getslope(dots[1], dots[2])
    slope2_2 = getslope(dots[0], dots[3])
    
    if slope1_1==slope1_2:
        answer = 1
    elif slope2_1==slope2_2:
        answer = 1
    else:
        answer = 0
        
    return answer