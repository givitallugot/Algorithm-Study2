import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/7. 창고 정리/in5.txt')

n = int(input())
strg = list(map(int, input().split()))
m = int(input())

for i in range(m):
    mx = max(strg)
    mn = min(strg)
    mxidx = [i for i, j in enumerate(strg) if j == mx][0]
    mnidx = [i for i, j in enumerate(strg) if j == mn][0]
    
    strg[mxidx] -= 1
    strg[mnidx] += 1

print(max(strg) - min(strg))