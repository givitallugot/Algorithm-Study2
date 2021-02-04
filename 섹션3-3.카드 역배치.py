import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/3. 카드 역배치/in5.txt')

numbers = list(range(1, 21))

for i in range(10):
    interval = list(map(int, input().split(sep=' ')))
    temp = numbers[interval[0]-1:interval[1]]
    numbers[interval[0]-1:interval[1]] = temp[::-1]

print(*numbers, sep=" ")