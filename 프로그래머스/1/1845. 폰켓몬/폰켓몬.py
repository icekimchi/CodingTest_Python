#3,1,2 중 2개
#3,2,4 중 3개
#3,2 중 3개
from collections import Counter

def solution(nums):
    answer = 0
    counts = Counter(nums).most_common()
    
    if len(counts)>len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(counts)
        
    return answer