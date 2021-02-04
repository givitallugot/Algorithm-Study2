import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/5. 수들의 합/in4.txt')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i, N):
        if sum(numbers[i:j+1]) == M:
            cnt += 1

print(cnt)

# 3, 4, 5는 오래걸림.. 뭐지 어려운걸?
# 더 최적화할 수 있는 방법..? CASE를 나눠야하나?