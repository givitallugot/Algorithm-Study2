import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/4. 마구간 정하기/in5.txt')

N, C = map(int, input().split())
stall = []

for i in range(N):
    stall.append(int(input()))
stall.sort()

start = max(stall)//(C-1)

for ml in range(start, -1, -1):
    lt = stall[0]
    c = 1
    for loc in stall:
        if (loc - lt) >= ml:
            lt = loc
            c += 1

    if c >= C:
        print(ml)
        break

