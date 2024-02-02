def solution(numbers, hand):
    n = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]
        
    left_key = [1, 4, 7]
    right_key = [3, 6, 9]
    
    pad = {}
    answer = ""
    
    for i, val_i in enumerate(n):
        for j, val_j in enumerate(val_i):
            pad[val_j] = (i, j)

    left_pos = (3, 0)
    right_pos = (3, 2)
    
    for number in numbers:
        x, y = pad[number]
        if number in left_key:
            left_pos = x, y
            answer += "L"
        elif number in right_key:
            right_pos = x, y
            answer += "R"
        else:
            right_distance = abs(right_pos[0] - x) + abs(right_pos[1] - y)
            left_distance = abs(left_pos[0] - x) + abs(left_pos[1] - y)
            if right_distance<left_distance:
                right_pos = x, y
                answer += "R"
            elif right_distance>left_distance:
                left_pos = x, y
                answer += "L"
            else:
                if hand=="right":
                    right_pos = x, y
                    answer += "R"
                else:
                    left_pos = x, y
                    answer += "L"
    return answer

