import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/15. 토마토/in5.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M,N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
dis = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            Q.append((i,j))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        nx = tmp[0]+dx[i]
        ny = tmp[1]+dy[i]
        if 0<=nx<N and 0<=ny<M and tomato[nx][ny]==0:
            tomato[nx][ny] = 1
            dis[nx][ny] = dis[tmp[0]][tmp[1]] + 1
            Q.append((nx,ny))

flag = 1
mx = 0
for i in range(N):
    if mx < max(dis[i]):
        mx = max(dis[i])
    for j in range(M):
        if tomato[i][j] == 0:
            flag = 0

if flag == 0:
    print(-1)
else:
    print(mx)