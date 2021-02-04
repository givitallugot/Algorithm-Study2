import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/2. 숫자만 추출/in5.txt')

S = str(input())
numbers = str(list(range(0,10)))
num = ''
cnt = 0

for s in S:
    if s in numbers:
        num += s

num = int(num)
print(num)

for n in range(1, num+1):
    if num % n == 0:
        cnt += 1

print(cnt)