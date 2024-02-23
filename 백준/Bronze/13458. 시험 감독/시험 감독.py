N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for student in A:
    if student<B:
        answer += 1
        continue
    else:
        student -= B
        answer += 1

        if student%C:
            answer += student//C + 1
        else:
            answer += student//C

print(answer)