import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/6. 씨름선수/in2.txt')

n = int(input())
wrestler = []
for _ in range(n):
    wrestler.append(list(map(int,input().split())))

wrestler.sort()
pick = [wrestler[0]]

for wres in wrestler[1:]:
    i = 0
    while True:
        if i >= len(pick):
            break
        if pick[i][1] < wres[1]:
            pick.pop(i)
            i -= 1
        i += 1
    pick.append(wres)

print(len(pick))