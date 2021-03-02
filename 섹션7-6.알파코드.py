import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/6. 알파코드/in5.txt')

def DFS(L, P):
    global n, cnt
    global res
    if L == n:
        for j in range(P):
            print(res[j], end='')
        print()
        cnt += 1
        return
    else:
        for i in range(1, 27):
            if i >= 10:
                LL = L + 2
            else:
                LL = L + 1
            if LL <= n:
                if (int(''.join(CODE[L:LL])) == i):
                    res[P] = chr(i+64)
                    DFS(LL, P+1)

if __name__ == "__main__":
    N = input()
    n = len(N)
    cnt = 0
    CODE = list(N)
    res = ['']*(n+3)
    DFS(0, 0)
    print(cnt)