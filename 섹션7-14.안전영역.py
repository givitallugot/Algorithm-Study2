# BFS 안풀림
import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/14. 안전영역/in1.txt')
sys.setrecursionlimit(10**6) # 파이썬에서 재귀를 돌릴 때 time limit을 설정해야 함

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
N=int(input())
A=[]
LOC=[]
for _ in range(N):
    l = list(map(int, input().split()))
    LOC.append(l)
    A = A + l

A.sort()
A = set(A)

cnt=0
maxloc=[]
Q=deque()
for height in A:
    TLOC = LOC
    cnt = 0
    print(height)
    for i in range(N):
        for j in range(N):
            if TLOC[i][j] > height:
                TLOC[i][j]=0
                Q.append((i, j))
                cnt+=1
                while Q:
                    tmp=Q.popleft()
                    for k in range(4):
                        x=tmp[0]+dx[k]
                        y=tmp[1]+dy[k]
                        if 0<=x<N and 0<=y<N and TLOC[x][y] > height:
                            TLOC[x][y]=0
                            Q.append((x, y))
    maxloc.append(cnt)

print(maxloc)
print(max(maxloc))



# DFS
import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/14. 안전영역/in1.txt')

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
sys.setrecursionlimit(10**6)
def DFS(x, y, h):
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx, yy, h)

if __name__=="__main__":
    n = int(input())
    cnt = 0
    res = 0
    board=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i, j, h)
        res=max(res, cnt)
        if cnt==0:
            break
    print(res)





    