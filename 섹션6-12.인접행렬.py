import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/12. 인접행렬/in1.txt')

N, M = map(int, input().split())
conlst = []
for i in range(N):
    conlst.append([0]*N)

for i in range(M):
    s, e, w = map(int, input().split())
    conlst[s-1][e-1] = w

for i in range(N):
    print(*conlst[i], sep=' ')

# 그래프: 노드와 간선의 집합
# 방향, 가중치 설정되면 '가중치 방향 그래프'