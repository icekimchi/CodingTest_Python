def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_set = set(dice)
    dice_list = list(dice_set)
    
    if len(dice_set)==1:
        return 1111*max(dice_list)
    elif len(dice_set)==2:
        for element in dice_list:
            if dice.count(element)==3:
                p = element
                dice_list.remove(p)
                q = max(dice_list)
                return (10 * p +q)* (10*p+q)
            elif dice.count(element)==2:
                p = element
                dice_list.remove(p)
                q = max(dice_list)
                return (p+q)*abs(p-q)
    elif len(dice_set)==3:
        for element in dice_list:
            if dice.count(element)==2:
                p = element
                dice_list.remove(p)
                return max(dice_list) * min(dice_list)
    else:
        return min(dice)
                
                
    
            
                
                    
                