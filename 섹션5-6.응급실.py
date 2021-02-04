import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/6. 응급실/in5.txt')

N, M = map(int, input().split())
pat = deque(list(map(int, input().split())))
loc = deque(list(range(N))) # 몇 번째 환자

i = 0 # 몇 번째 진료
while pat:
    mx = max(pat)
    if pat[0] == mx:
        i += 1
        pat.popleft()
        l = loc.popleft()
        if l == M:
            print(i)
            break
    else:
        pat.append(pat.popleft())
        loc.append(loc.popleft())
    
