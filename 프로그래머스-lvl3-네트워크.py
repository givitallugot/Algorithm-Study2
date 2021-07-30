# 다시 풀어보면 좋을 문제, DFS로도?

from collections import deque
def solution(n, computers):
    answer = 0
    queue = deque()
    computers = deque(computers)
    # queue.append(computers.popleft())
    
    for i, ilist in enumerate(computers):
        queue.append(computers.popleft())
                     
        while queue:
            now = queue.popleft()
            for j in range(n):
                if (now[j] == 1) & (j != i):
                     queue.append(computers.pop(j))
        else:
            answer += 1
    return answer

    ### 
    ### https://dev-note-97.tistory.com/149?category=884288 참고


    # from collections import deque
def solution(n, computers):
    answer = 0
    network = [False for n in range(n)]
    Q = [0] # 첫 번째 노드부터
    
    while True: # 전체 노드
        while Q: # 특정 노드랑 연결된 노드들 찾기
            node = Q.pop(0)
            if not network[node]:
                network[node] = True
                for i in range(n):
                    if computers[node][i] == 1:
                        Q.append(i)
                    
        if all(network): # all true인 경우 모두 방문 완료
            answer += 1
            break
        else:
            answer += 1
            Q = [network.index(False)]

    return answer