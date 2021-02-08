import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/6. 중복순열 구하기/in5.txt')

def DFS(i, j, l):
    global L
    if i == M+1:
        if l not in L:
            print(*l, sep=' ')
            L.append(l)
        return
    else:
        for j in range(1, N+1):
            DFS(i+1, j, l+[j])


if __name__ == "__main__":
    N, M = map(int, input().split())
    L = []
    for j in range(1, N+1):
        DFS(1, j, [])
    print(len(L))
    