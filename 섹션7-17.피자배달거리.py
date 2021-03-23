import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/17. 피자 배달 거리/in2.txt')


def DFS(L, s):
    global res
    if L==m:
        sum=0
        for j in range(len(hs)):
            # 집의 좌표
            x1=hs[j][0]
            y1=hs[j][1]
            dis=2147000000

            for x in cb: # M개, 가능한 피자집 조합
                # 피자집 좌표
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if sum<res:
            res=sum    
    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1, i+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    hs=[]
    pz=[]
    cb=[0]*m
    res=2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)