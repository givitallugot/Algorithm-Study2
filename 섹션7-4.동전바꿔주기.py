import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/4. 동전바꿔주기/in1.txt')

def DFS(L, sm):
    global N, K, cnt
    if L == N:
        if sm == T:
            cnt = cnt + 1
            print(sm)
        return
    elif sm > T:
        return
    else:
        DFS(L+1, sm+ch[L])
        DFS(L+1, sm)

if __name__ == '__main__':
    T = int(input())
    K = int(input())
    ch = []
    for i in range(K):
        p, n = map(int, input().split())

        for j in range(n):
            ch.append(p)
    N = len(ch)
    cnt = 0
    print(T, K)
    DFS(0, 0)
    print(cnt)