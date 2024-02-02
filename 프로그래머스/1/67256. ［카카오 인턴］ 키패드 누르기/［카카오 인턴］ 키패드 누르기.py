def solution(numbers, hand):
    n = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
        
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    
    pad = {}
    answer = ""
    
    for i, val_i in enumerate(n):
        for j, val_j in enumerate(val_i):
            pad[val_j] = (i, j)

    l_pos = (3, 0)
    r_pos = (3, 2)
    
    for number in numbers:
        x, y = pad[number]
        if number in left_key:
            l_pos = x, y
            answer += "L"
        elif number in right_key:
            r_pos = x, y
            answer += "R"
        else:
            r_distance = abs(r_pos[0] - x) + abs(r_pos[1] - y)
            l_distance = abs(l_pos[0] - x) + abs(l_pos[1] - y)
            
            if r_distance<l_distance:
                r_pos = x, y
                answer += "R"
            elif r_distance>l_distance:
                l_pos = x, y
                answer += "L"
            else:
                if hand=="right":
                    r_pos = x, y
                    answer += "R"
                else:
                    l_pos = x, y
                    answer += "L"
    return answer

