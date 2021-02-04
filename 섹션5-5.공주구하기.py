import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/5. 공주구하기/in2.txt')

N, K = map(int, input().split())
prince = deque(list(range(1,N+1)))

i = 1
while len(prince) > 1:
    if i == K:
        i = 1
        prince.popleft()
    else:
        i += 1
        prince.append(prince.popleft())

print(prince[0])