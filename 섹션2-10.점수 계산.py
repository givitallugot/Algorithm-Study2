import sys
# sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/10. 점수 계산/in5.txt", "rt")

N = int(input())
result = list(map(int, input().split()))

j = 0
score = []
for i in range(N):
    if result[i] == 1:
        j = j+1
        score.append(j)
    else:
        j = 0

print(sum(score))