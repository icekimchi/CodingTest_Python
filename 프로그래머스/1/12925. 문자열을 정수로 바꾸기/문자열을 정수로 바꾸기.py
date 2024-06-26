def solution(s):
    if s[:1]=="-":
        return -int(s[1:])
    else:
        return int(s)
