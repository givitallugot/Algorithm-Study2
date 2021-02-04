import sys
import heapq as hq
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/11. 최대힙/in2.txt')

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0: # 데이터 없을 때
            print(-1)
        else:
            print(hq.heappop(a)[1]) # a에서 루트 노드 값을 pop
    else:
        hq.heappush(a, (-n, n))
