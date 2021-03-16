import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/13. 섬나라 아일랜드/in5.txt')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i,j))
            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0]+dx[k]
                    y = tmp[0]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x,y))
            cnt += 1 # 섬 하나 개수 추가


print(cnt)
