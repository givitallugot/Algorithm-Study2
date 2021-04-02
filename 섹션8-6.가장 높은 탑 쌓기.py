import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/6. 가장 높은 탑 쌓기(LIS 응용)/in4.txt')

N = int(input())
brick = [list(map(int, input().split())) for _ in range(N)]
brick.sort(reverse=True) # **
brick.insert(0,[0,0,0])
dy = [0]*(N+1)
dy[1] = brick[1][1]
# 0번째에 0, 1번째에 처음 원소 초기화 필요

for i in range(2, N+1):
    maxdy = 0
    for j in range(i-1, 0, -1):
        if (brick[i][0] < brick[j][0]) and (brick[i][2] < brick[j][2]) and (maxdy < dy[j]):
            maxdy = dy[j]
    dy[i] = maxdy + brick[i][1]

print(N)
print(brick)
print(dy)

print(max(dy))

# 피드백: 높이 기준으로 sort 하고, 무게 기준만 맞추는 방식으로 해야 함.

# dy[2]란 2번 벽돌을 가장 꼭대기에 놓았을 때 최대 높이
# dy[4]란 4번 벽돌을 가장 꼭대기에 놓았을 때 최대 높이