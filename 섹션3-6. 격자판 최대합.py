import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/6. 격자판 최대합/in5.txt')

N = int(input())
dice = []
num = []

for i in range(N):
    dice.append(list(map(int, input().split())))

# 먼저 행(i) 확인
for i in range(N):
    num.append(sum(dice[i]))

# 열(j) 확인
for j in range(N):
    num.append(sum([dice[i][j] for i in range(N)]))

# 대각선 확인
temp = 0
for k in range(N):
    temp += dice[k][k]
num.append(temp)

temp = 0
for k in range(N):
    temp += dice[k][N-k-1]
num.append(temp)

print(max(num))