# kruskal Algorithm
# 탐욕법(그리디), 사이클 X, 정렬 필수

def solution(n, costs):
    answer = 0
    costL = [-1]*n
    costs.sort(key=lambda x: x[2])
    
    connections = [costs[0][0]]
    
    while len(connections) != n:

        for i, cost in enumerate(costs):
            # 이미 최소 거리 찾아진 경우
            if (cost[0] in connections) and (cost[1] in connections):
                continue
            
            # 최소 거리 찾지 못한 경우 (한 쪽만 들어간 경우)
            if (cost[0] in connections) or (cost[1] in connections):
                connections.append(cost[0])
                connections.append(cost[1])
                answer += cost[2]
                costs.pop(i)
                connections = list(set(connections))
                break
    return answer