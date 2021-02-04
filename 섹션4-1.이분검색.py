import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/1. 이분검색/in5.txt')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

i = N
loc = 0
while True:
    i = int(i/2+0.5)
    if numbers[i-1] == M:
        loc = loc + i
        print(loc)
        break
    elif numbers[i-1] > M:
        numbers = numbers[:i-1]
    elif numbers[i-1] < M:
        numbers = numbers[i:]
        loc = loc + i