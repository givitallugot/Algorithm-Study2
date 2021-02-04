import sys
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/7. 소수(에라토스테네스 체)/in2.txt", "rt")

N = int(input())

def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

sosu = []
for i in range(2, N+1):
    if isPrime(i):
        sosu.append(i)

print(len(sosu))

# 개오래걸림, 에라토스테네스 체가 무엇인지 확인