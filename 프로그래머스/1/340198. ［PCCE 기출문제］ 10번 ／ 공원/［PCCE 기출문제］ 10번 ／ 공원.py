def test(x, y, park, mat):
    for i in range(mat):
        for j in range(mat):
            if x + i >= len(park[0]) or y + j >= len(park):
                return False
            if park[y + j][x + i] != "-1":
                return False
    return True

def solution(mats, park):
    width = len(park[0])
    height = len(park)
    mats = sorted(mats, reverse=True)
    
    for mat in mats:
        for y in range(height):
            for x in range(width):
                if y + mat <= height and x + mat <= width: 
                    if test(x, y, park, mat):
                        return mat
                    
    return -1