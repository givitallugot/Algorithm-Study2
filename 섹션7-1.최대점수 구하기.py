import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/1. 최대점수 구하기/in1.txt')

def DFS(L, ssum, tsum):
    global smax
    if (ssum > smax) and (tsum <= M):
        smax = ssum
        print(res, smax, tsum)
    else:
        for j in range(N):
            if ch[j] == 0:
                ch[j] = 1
                res[j] = score[j]
                DFS(j+1, ssum + score[i], tsum + time[i])    
                ch[j] = 0

if __name__ == '__main__':
    N, M = map(int, input().split()) # 개수, 점수
    score = [0]*N
    time = [0]*N
    ch = [0]*N
    res = [0]*N
    smax = 0
    for i in range(N):
        score[i], time[i] = map(int, input().split())
    
    DFS(0, 0, 0)
    print(smax)

    # 이렇게 풀면 안되고, 넣을건지 안넣을건지, 부분집합에 관한 내용 (순열 X, 조합 X)