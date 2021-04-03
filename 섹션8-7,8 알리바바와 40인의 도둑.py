import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/7, 8. 알리바바와 40인의 도둑/in0.txt')

N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]
D = [[0]*N for _ in range(N)]
D[0][0] = R[0][0]

dx = [1, 0] # 행
dy = [0, 1] # 열

Q = deque()
Q.append((0,0))
L = 0

while Q:
    now = Q.popleft()
    if now == (N-1, N-1):
        break
    
    print(now)
    mn = 10; newx = 0; newy = 0
    for i in range(2):
        x = now[0] + dx[i]
        y = now[1] + dy[i]

        if x < N and y < N and R[x][y] < mn:
            mn = R[x][y]
            newx = x
            newy = y
    
    Q.append((newx, newy))
    D[newx][newy] = D[now[0]][now[1]] + mn

print(D[N-1][N-1])
print(D)

# 현재 위치에서 최선을 찾는 방법 (그리디 서치) != 현재 위치까지 오는 방법 중 가장 최선 (다이나믹)

