import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/1. 회문 문자열 검사/in5.txt')

N = int(input())

for i in range(N):
    word = str(input())
    if word.lower() == word[::-1].lower():
        print('#{0} YES'.format(i+1))
    else:
        print('#{0} NO'.format(i+1))