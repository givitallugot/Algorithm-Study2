import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/10. 조합 구하기/in5.txt')

def DFS(L, C):
    global cnt
    if L == M:
        print(*C[1:], sep=' ')
        cnt = cnt + 1
    else:
        for i in range(N):
            if (ch[i] == 0) & (C[-1] < i+1):
                ch[i] = 1
                DFS(L+1, C+[i+1])
                ch[i] = 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    ch = [0]*N
    cnt = 0
    DFS(0, [0])
    print(cnt)

# 중요힌 문제