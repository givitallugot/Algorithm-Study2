import sys
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/2. k번째 수/in5.txt", "rt")

T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(i+1, sorted(numbers[s-1:e])[k-1])