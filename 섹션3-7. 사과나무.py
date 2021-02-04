import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/7. 사과나무/in5.txt')

N = int(input())
apple = []
total = 0
bird = 0

for _ in range(N):
    a = list(map(int, input().split()))
    total += sum(a)
    apple.append(a)

for i in range(N//2):
    for j in range((N//2-i)):
        bird += apple[i][j] # 왼-위
        bird += apple[i][N-j-1] # 오-위
        bird += apple[N-i-1][j] # 왼-아래
        bird += apple[N-i-1][N-j-1]

print(total-bird)
