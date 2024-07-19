def solution(bandage, health, attacks):
    
    ban_time, dhealth, bonus = bandage
    hp = health
    attack_time = 0
    
    for i, attack in enumerate(attacks):
        if hp<=0:
            return -1
            
        if i>0:
            attack_time = attacks[i][0] - attacks[i-1][0] 
        
        time, damage = attack
        
        if attack_time>1:
            for bandage_time in range(1, attack_time):
                hp += dhealth
                if bandage_time%ban_time==0:
                    hp += bonus
                hp = min(health, hp)
        print("공격 전까지 회복한 ph :", hp)
            
        hp -= damage
        print("공격한 후 남은 ph: ", hp)
        
    return -1 if hp<=0 else hp