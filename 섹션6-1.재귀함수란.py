import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 6/1. 재귀함수란(이진수출력)/in3.txt')
N = int(input())

bin = []
def binary(x):
    if x != 0:
        bin.append(x % 2)
        binary(x // 2)
    else:
        print(*bin[::-1], sep='')

binary(N)