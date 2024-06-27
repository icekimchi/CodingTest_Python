def solution(n):
    x = list(map(int, list(str(n))))
    x = list(map(str, sorted(x, reverse=True)))
    return int(''.join(x))

