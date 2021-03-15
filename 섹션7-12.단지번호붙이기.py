import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/12. 단지번호붙이기/in2.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x,y):
    global cnt
    cnt += 1 # 처음 하나의 집 넘어옴
    board[x][y] = 0 # 중복 방문 방지
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx,yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)