N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

#버블 정렬
for i in range(N):
    for j in range(i+1, N):
        if num[i]>num[j]:
            num[i], num[j] = num[j], num[i]

for answer in num:
    print(answer)
