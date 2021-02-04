import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/7. 교육과정 설계/in5.txt')

need = list(input())
n = int(input())

for i in range(n):
    design = deque(list(input()))
    tmp = deque(need)
    while design and tmp:
        j = design.popleft()
        if j == tmp[0]: # 첫번째
            tmp.popleft()
        elif j in tmp: # 첫번째 아님
            break
    if len(tmp) == 0:
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))