def lcm(x, y):
    for k in range(max(x, y), x*y+1):
        if k%x==0 and k%y==0:
            return k

def gcd(x, y):
    for k in range(min(x, y), 0, -1):
        if x%k==0 and y%k==0:
            return k

def solution(numer1, denom1, numer2, denom2):
    
    k = lcm(denom1, denom2)
    numer1 *= k//denom1
    numer2 *= k//denom2
    
    l = gcd(numer1 + numer2, k)
    
    return [(numer1 + numer2)/l, k/l]