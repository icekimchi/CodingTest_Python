def DFS(temp, dict, answer, ticket_count):
    while dict.get(temp):   #키가 존재할 때까지
        next_dest = dict[temp].pop(0)  #dict에서 뽑아서 사용
        DFS(next_dest, dict, answer, ticket_count) #그 다음 경로로 재귀 사용
    
    # 이 코드가 실행된다는 것은 while문에서 False가 나왔을 때
    # 즉, 전체 경로를 모두 탐색하면 append 함수가 실행된다.
    answer.append(temp)  # 경로를 끝에서부터 쌓아가야 함 (백트래킹)
    

def solution(tickets):
    answer = []
    dict = {}
    
    for start, dest in tickets:
        if start in dict:
            dict[start].append(dest)
        else:
            dict[start] = [dest]
            
    for start in dict:
        dict[start].sort()
    
    # DFS 탐색 시작
    DFS("ICN", dict, answer, len(tickets))
    
    return answer[::-1]  # 거꾸로 출력해야 올바른 경로가 나옴