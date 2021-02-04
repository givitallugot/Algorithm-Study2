import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/2. 랜선자르기/in5.txt')

K, N = map(int, input().split())
lan = []

for i in range(K):
    lan.append(int(input()))

start = sum(lan)//N
m = start
for i in range(start):
    n = 0

    for l in lan:
        n += l//m
    
    if n >= N:
        print(m)
        break
    
    m -= 1
