def solution(clothes):
    outfits = {}
    count = 1
    
    for cloth in clothes:
        if cloth[1] in outfits:
            outfits[cloth[1]].append(cloth[0])
        else:
            outfits[cloth[1]] = [cloth[0]]
    
    for i in outfits:
        count *= len(outfits[i])+1
            

    return count -1