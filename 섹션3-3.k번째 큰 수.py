import sys
from itertools import combinations
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/3. k번째 큰 수/in1.txt", "rt")

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

nC3 = list(combinations(numbers, 3))
sum_nC3 = sorted(set([sum(i) for i in nC3]), reverse=True) # set을 취해서 unique하게 만든 후 sorted로 list 반환
print(sum_nC3[K-1])