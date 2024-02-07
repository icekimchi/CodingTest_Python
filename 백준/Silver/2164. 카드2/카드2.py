import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([a for a in range(1, N+1)])

while len(card)>1:
    card.popleft() #del card[0]
    card.append(card.popleft()) #card.append(card.pop(0))

print(card[0])