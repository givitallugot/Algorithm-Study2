import sys
import collections
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/9. 아나그램(구글)/in5.txt')

A = list(input())
B = list(input())

if list(collections.Counter(A) - collections.Counter(B))==[]:
    print('YES')
else:
    print('NO')