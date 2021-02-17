import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/11. 수들의 조합/in5.txt')

def DFS(L, W):
    global cnt
    if L == K:
        sm = sum(res)
        if (sm % M) == 0:
            cnt = cnt + 1
            print(res)
    else:
        for i in range(W, N+1):
            res[L] = num[i-1]
            DFS(L+1, i+1)

if __name__ == '__main__':
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    M = int(input())
    cnt = 0
    res = [0] * K

    DFS(0, 1)
    print(cnt)