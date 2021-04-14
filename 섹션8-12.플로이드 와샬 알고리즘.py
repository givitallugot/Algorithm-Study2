import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/12. 플로이드 워샬 알고리즘/in1.txt')

# 플로이드 와샬 알고리즘, 냅색 알고리즘과 비슷함
# dis[i][j]: i 정점에서 j 정점으로 가는 최소 비용
# dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]) # 즉 i에서 j로 가는데 k를 거쳐서 간 것
# 이때 순서가 2->1->3일 수도, 즉 k가 i보다 작을 수도
# 5->4일 때, 5->2->3->1->4 이런 식으로도 갈 수 있음
# 5->3->3도 가능, 3->3은 0이므로
 
if __name__=="__main__":
    n, m=map(int, input().split())
    dis=[[5000]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1): # 자기 자신으로 가는 것은 0으로 초기화
        dis[i][i]=0
    
    for i in range(m): # 중간에서 아무것도 들리지 않고 직행했을 때 갈 수 있는 값, 못가면 M으로 여전히 남아있을 것
        a, b, c=map(int, input().split())
        dis[a][b]=c

    for k in range(1, n+1): # 플로이드와샬 알고리즘, k에 따라 i, j 이중 for문이 돌면서 값 갱신
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j]) # 기존값보다 i->k->j가 더 작으면 바꿔줌

    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j]==5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()