import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/8. 침몰하는 타이타닉/in5.txt')

N, M = map(int, input().split())
boat = list(map(int, input().split()))
boat.sort()

bcnt = 0
while len(boat) > 0:
    gap = M - boat[-1]
    if (boat[0] <= gap) and (len(boat) != 1):
        boat.pop(0)
        boat.pop(-1)
        bcnt += 1
    else:
        boat.pop(-1)
        bcnt += 1

print(bcnt)