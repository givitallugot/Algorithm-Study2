import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/2. 휴가/in4.txt')

def DFS(L, sm):
    global pmax
    global N

    if L == N:
        if sm > pmax:
            pmax = sm
        return
    else:
        if (L+T[L] <= N):
            DFS(L+T[L], sm + P[L])
        DFS(L+1, sm)



if __name__ == '__main__':
    N = int(input())
    T = [0]*N
    P = [0]*N
    res = [0]*N
    pmax = 0

    for i in range(N):
        T[i], P[i] = map(int,input().split())
    
    print(T, P)
    # T = [4, 2, 3, 3, 2, 2, 1]
    # P = [20, 10, 15, 20, 30, 20, 10]

    DFS(0, 0)
    print(pmax)