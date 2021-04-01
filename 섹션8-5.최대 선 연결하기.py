# Longest Increasing Sequence: 최대부분 증가수열

import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/5. 최대 선 연결하기/in5.txt')

N = int(input())
L = list(map(int, input().split()))

L.insert(0, 0)
dy = [0]*(N+1)
dy[1] = 1

for i in range(2, N+1):
    dymax = 0
    for j in range(i-1, 0, -1):
        if (L[i] > L[j]) and (dy[j] > dymax):
            dymax = dy[j]
    dy[i] = dymax + 1

print(L)
print(dy)

print(max(dy))