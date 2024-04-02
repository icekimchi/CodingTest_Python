def solution(wallpaper):
    r = []
    c = []
    
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[row])):
            if wallpaper[row][col] == "#":
                r.append(row)
                c.append(col)
    
    return [min(r), min(c), max(r) + 1, max(c) + 1]