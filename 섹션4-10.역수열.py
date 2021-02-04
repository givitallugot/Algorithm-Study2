import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/10. 역수열/in5.txt')

n = int(input())
serial = list(map(int, input().split()))
serial = serial[::-1]

tmp = []
for i in range(n):
    tmp.insert(serial[i], n-i) # serial[i] 자리에 n-i 추가

print(tmp)