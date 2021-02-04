import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/9. 증가수열 만들기/in5.txt')

N = int(input())
l = list(map(int, input().split()))
result = ''
last = 0

if l[0] > l[-1]:
    result = 'R'
    last = l.pop(-1)
else:
    result = 'L'
    last = l.pop(0)

while len(l) != 0:
    if (last >= l[0]) and (last >= l[-1]):
        break
    else:
        if (last < l[0]) and (l[0] < l[-1]):
            result += 'LR'
            l.pop(0)
            last = l.pop(-1)
        elif (last < l[-1]) and (l[-1] < l[0]):
            result += 'RL'
            l.pop(-1)
            last = l.pop(0)
        elif last < l[0]:
            result += 'L'
            last = l.pop(0)
        elif last < l[-1]:
            result += 'R'
            last = l.pop(-1)

print(len(result))
print(result)