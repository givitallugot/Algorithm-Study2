import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/11. 최대점수 구하기(냅색알고리즘)/in2.txt')

# 각 문제 (s-점수, t-걸리는 시간)
# dy[i] = max(dy[i], dy[i-t] + s)
# dy는 모두 0으로 초기화

if __name__ == '__main__':
    N, M = map(int, input().split())
    problems = [list(map(int, input().split())) for _ in range(N)]

    dy=[0]*(M+1)
    for [s,t] in problems:
        for j in range(t, M+1):
            dy[j] = max(dy[j], dy[j-t] + s)

    print(dy)

    print(dy[M])

# 한 유형 당 하나만 풀 수 있다는 것이 포인트! (아래 코드를 이용해야 함)

import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/11. 최대점수 구하기(냅색알고리즘)/in5.txt')

# 각 문제가 각 유형임
# dy가 이차원 테이블, dy[i][j]: i번째 문제 종료까지 적용했고, 주어진 시간이 j일 때 최대 점수를 기록
# dy[3][15] 라면 3번째 유형까지 적용했고, M이 15라면 얻을 수 있는 최대값

# 0 1 2 3 4  5  6  7  8  9  10 ... 20 (index)
# 0 0 0 0 0  0  0  0  0  0  0  ... 0  - 첫 번째 행
# 0 0 0 0 0 10 10 10 10 20(이게 안됨.. 두 번 쓴것) - 두 번째 행 (첫번째 유형 적용)
# (생략)

# 따라서 dy[i][j]를 넣기 위해 dy[i-1][j]를 참조해야 됨, i번째 유형을 지금 이용하고 있기 때문에.
# dy[i][j] = dy[i-1][j-t] 으로 적용하고
# i번째 문제를 적용하기 전에, i-1번째 행 값을 모두 복사해두고 시작하기
# (즉 유형 하나씩만 쓸 때 i번째 유형까지 풀었을 때 최대값들을 일단 넣어두고 신 유형 적용)

if __name__ == '__main__':
    N, M = map(int, input().split())
    problems = [list(map(int, input().split())) for _ in range(N)]

    dy=[[0]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        dy[i] = dy[i-1].copy() # 그냥 dy[i] = dy[i-1] 는 주소복사가 됨!

        [s,t] = problems[i-1]
        for j in range(t, M+1):
            dy[i][j] = max(dy[i][j], dy[i-1][j-t] + s)
        
        # 확인용 출력
        for i in range(N+1):
            print(dy[i])
        print(' ')

    print(dy[N][M])