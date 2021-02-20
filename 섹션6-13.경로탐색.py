import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/13. 경로탐색/in5.txt')

def DFS(L):
    global cnt
    if L == N:
        cnt = cnt + 1
        print(ch)
        return
    else:
        for n in range(1,N+1):
            if (G[L-1][n-1] == 1) and (ch[n-1] == 0):
                ch[n-1] = 1
                DFS(n)
                ch[n-1] = 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    cnt = 0 # 중복 체크, 한번 거친 노드는 다시 돌아오지 않도록
    G = []*N
    ch = [0]*N
    ch[0] = 1

    for _ in range(N):
        G.append([0]*N)

    for _ in range(M):
        s, e = map(int, input().split())
        G[s-1][e-1] = 1

    DFS(1)
    print(cnt)