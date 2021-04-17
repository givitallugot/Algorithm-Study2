import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/13. 회장뽑기/in2.txt')

# dis[][] 그래프의 최단 거리를 구하는 것, 가까움의 정도는 더 짧은 거리 기준
# 최소값을 찾으면 회장 후보가 됨
# res[] 각 사람별(회장후보별) 점수
# 최솟값 & 최솟값 counting

if __name__ == "__main__":
    n = int(input())
    dis = [[100]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dis[a][b] = 1
        dis[b][a] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    # 여기까지 Distance Matrix 완성
    print(dis)
    
    res=[0]*(n+1)
    score=100
    for i in range(1, n+1):
        for j in range(1, n+1):
            res[i]=max(res[i], dis[i][j])
        score=min(score, res[i])
    out=[]
    for i in range(1, n+1):
        if res[i]==score:
            out.append(i)
    print("%d %d" %(score, len(out)))
    for x in out:
        print(x, end=' ')