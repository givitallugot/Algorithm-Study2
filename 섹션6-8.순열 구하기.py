import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/8. 순열 구하기/in2.txt')

def DFS(L, marbl):
    global cnt
    if L == M:
        cnt =  cnt + 1
        print(*res, sep=' ')
        return
    else:
        for j in range(len(marbl)):
            res[L] = marbl[j]
            new_marbl = [x for i,x in enumerate(marbl) if i!=j]
            DFS(L+1, new_marbl)

if __name__ == '__main__':
    N, M = map(int, input().split())
    res = [0]*M
    marble = list(range(1,N+1))
    cnt = 0
    DFS(0, marble)
    print(cnt)

# check list를 만드는 것을 추천
    
