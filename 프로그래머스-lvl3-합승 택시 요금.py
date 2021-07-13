### 그래프의 최단 거리 문제, 플로이드-와샬, 다익스트라필요 ###

# 아래는 플로이드 와샬로 푸는 방법
# 비용(S - K) + 비용(K - A) + 비용(K - B)의 최소, 임의의 K 이후 A, B로 갈라지는 형태 (시작은 같으므로)
# 다시 풀기 + 비슷한 문제 풀기 + 다익스트라로 풀기

import sys
input = sys.stdin.readline


def solution(n, s, a, b, fares):
    INF = int(1e9)                                  #무한을 의미하는 값 10억 설정
    graph = [[INF] * n for _ in range(n)]			

    for i in range(n):                              #자기 자신으로 가는 비용 0
        graph[i][i] = 0

    for i in fares:
        graph[i[0] - 1][i[1] - 1] = i[2]            #이동 방향에 따라 비용이 달라지지 않으므로
        graph[i[1] - 1][i[0] - 1] = i[2]			

    for t in range(n):
        for i in range(n):
            for j in range(i, n):                   
                if i != j:                          #최소 비용 계산
                    temp = min(graph[i][j], graph[i][t] + graph[t][j]) 
                    graph[i][j] = graph[j][i] = temp

    answer = INF
    for t in range(n):                              #경유점에 따라 최소 합승 비용 탐색
        temp = graph[s - 1][t] + graph[t][b - 1] + graph[t][a - 1]      
        answer = min(answer, temp)

    return answer


# 틀린 풀이
from itertools import combinations_with_replacement,product

def DFS(a, b, a_next, b_next, fares_dict, price):
    global min_price
    
    if (a_next == a) and (b_next == b):
        if price < min_price:
            min_price = price
        return
    elif price >= min_price:
        return
    else:
        if a_next == b_next:
            combi_list = list(combinations_with_replacement(fares_dict[a_next],2))
            for combi in combi_list:
                if combi[0][0] == combi[1][0]:
                    price += combi[0][1] # 가격 같음
                else:
                    price += (combi[0][1] + combi[1][1]) # 가격 다름
                a_next = combi[0][0]
                b_next = combi[1][0]
                DFS(a, b, a_next, b_next, fares_dict, price)
        else:
            prod_list = list(product(fares_dict[a_next],fares_dict[b_next]))
            for prod in prod_list:
                price += (prod[0][1] + prod[1][1]) # 가격은 무조건 다름
                a_next = prod[0][0]
                b_next = prod[1][0]
                DFS(a, b, a_next, b_next, fares_dict, price)

# Maximum Recursion Error 발생
# 1. 한 번 들렸던 곳은 가면 안됨, 
# 2. A나 B 둘 중 먼저 도착하면 더 이상 움직이면 안됨

min_price = 100000

def solution(n, s, a, b, fares):
    global min_price
    answer = 0
    fares_dict = {}
    for i in range(n):
        fares_dict[i+1] = []

    for f in fares:
        fares_dict[f[0]].append([f[1], f[2]])
        fares_dict[f[1]].append([f[0], f[2]])
    
    DFS(a, b, s, s, fares_dict, 0)
        
    answer = min_price
    return answer


