import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/9. 미로의 최단거리 통로/in1.txt')

miro = []
for i in range(7):
    miro.append(list(map(int, input().split())))
# 아래, 옆 순서로
dx = [1, 0]
dy = [0, 1]
ch = [[0]*7 for _ in range(7)]
mnr = 0

Q = deque()
Q.append((0,0))

while True:
    if Q[-1] == (6,6):
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(2):
            print(tmp)
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if (miro[x][y] == 0) and (ch[x][y] == 0):
                mnr += 1
                ch[x][y] = 1
                Q.append((x,y))
    
print(mnr)

##### 

import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/9. 미로의 최단거리 통로/in5.txt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 위 부터 시계방향
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q = deque()
Q.append((0,0))
board[0][0] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            Q.append((x,y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
