import sys
from itertools import combinations
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/9. 수열 추측하기/in5.txt')

def DFS(L):
    if L == N:
        temp = 0
        for i in range(N):
            temp += P[i]*B[i]
        if temp == F:
            print(*P, sep='')
            sys.exit(0)
        return
    else:
        for i in range(1, N+1):
            if ch[i] == 0:
                ch[i] = 1
                P[L] = i
                DFS(L+1)
                ch[i] = 0 # 호출 후 되돌아와서, 위의 1 체크를 0으로 풀어줌

if __name__ == "__main__":
    N, F = map(int, input().split())
    P = [0]*N # 입력 숫자
    B = [0]*N # 이항 계수, 파스칼의 삼각형에서 더해지는 규칙을 이용하기 위해서
    for i in range(N):
        B[i] = len(list(combinations(list(range(1,N)), i))) # 이항 계수를 구함

    ch = [0]*(N+1) # check list

    DFS(0)