import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/1. 가장 큰 수/in5.txt')

num, n = map(int, input().split())

sl = []; tmp = num
for i in range(len(str(num))):
    sl.append([tmp % 10,i+1])
    tmp = tmp // 10
sl.sort(reverse=True)

mn = len(str(num))-n
last = len(str(num)) + 1
result = ''

for i in range(mn, 0, -1): # 줄어들면서 현재 자리 수를 나타냄
    for l in sl:
        if (l[1] >= i) and (l[1] < last):
            result += str(l[0])
            last = l[1]
            sl.remove(l)
            break

print(result)
        