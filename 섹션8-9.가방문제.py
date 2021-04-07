import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/9. 가방문제/in5.txt')

# 냅색 알고리즘
# dy[j]: 가방에 j라는 무게까지 담을 수 있을 때, 이 가방에 담을 수 있는 최대 가치
# 처음 초기화는 모두 0으로 (가치 0)
# 최대 무개가 11이라면 크기 12의 dy를 생성하고 모든 simul을 돌고 난 후 dy[11]의 값 출력하면 됨

# Sim 1 (5,12) = (w,v)
# dy[w] 위치부터 바꾸기 시작하면 됨
# dy[j] = dy[j-w] + v # 무게w 보석을 담는다고 가정했으므로 무게w를 일단 뺀 dy[j-w]에 보석 가치 v를 더한다.
# 0 0 0 0 0 12 12 12 12 12 24 24 우리는 dy[11]이 되어야함

# Sim 2 (3,8) = (w,v)
# dy[3] 위치부터 바꾸기 시작하면 됨
# dy[j] = dy[j-w] + v, w=3 v=8
# dy[j]에 대입할 때, 현재 값이 더 크면 바꾸지 않고 새롭게 제안된 값이 더 크면 바꿈
# 0 0 0 8 8 12 16 16 20 24 24 28

# ... 모든 보석에 대해 이를 수행

# 이렇게하면 최대가 되는 중복조합(?)을 찾을 수 있나봄
# 같은 보석을 여러 개 쓰는 것도, 다른 보석들 같이 사용하는 것도 가능한 것!
# 매 시뮬에서 가방 무게에 따른 보석 가치의 최대값을 계속 구함
# 이 매우 중요한 알고리즘!


if __name__ == "__main__":
    N, M = map(int, input().split())
    jewelry = [list(map(int, input().split())) for i in range(N)]
    dy = [0]*(M+1)
    for i in range(N):
        [w, v] = jewelry[i]
        for j in range(w, M+1):
            newval = dy[j-w] + v
            if newval > dy[j]:
                dy[j] = newval

    print(dy[M])