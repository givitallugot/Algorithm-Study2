# 미로 탈출
from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, list(input()))) for i in range(5)]

print(miro)

# 5 6 
# 101010
# 111111
# 000001
# 111111
# 111111

dr = [-1,0,1,0]
dc = [0,1,0,-1]

Q = deque([])
Q.append((0,0))

while Q:
    now = Q.popleft()

    if now == (n-1, m-1):
        break

    for i in range(4):
        if now[0] + dr[i] < 0 or now[0] + dr[i] >= n or now[1] + dc[i] < 0 or now[1] + dc[i] >= m: # 벽이 아니고
            continue
        if miro[now[0] + dr[i]][now[1] + dc[i]] == 1: # 해당 노드 처음 방문하는 경우에만, (0,0)으로부터의 거리 적는 것
            miro[now[0] + dr[i]][now[1] + dc[i]] = miro[now[0]][now[1]] + 1
            Q.append((now[0] + dr[i],now[1] + dc[i]))

print(miro)
print(miro[n-1][m-1])
