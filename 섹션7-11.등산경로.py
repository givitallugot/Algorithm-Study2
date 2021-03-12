import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/11. 등산경로/in5.txt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt, N
    if route[x][y] == end:
        cnt +=1
        return
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<N and 0<=yy<N and ch[xx][yy]==0 and route[x][y] < route[xx][yy]:
                ch[xx][yy] = 1
                DFS(xx,yy)
                ch[xx][yy] = 0



if __name__ == '__main__':
    start = 214000000
    end = -214000000
    sx, sy = 0, 0
    route = []
    cnt = 0
    N = int(input())
    ch = [[0]*N for _ in range(N)]
    
    for i in range(N):
        new = list(map(int,input().split()))
        if start > min(new):
            start = min(new)
            sx = i
            sy = new.index(min(new))
        if end < max(new):
            end = max(new)
        route.append(new)

    ch[sx][sy] = 1

    DFS(sx,sy)
    print(cnt)