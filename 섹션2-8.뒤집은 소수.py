import sys
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/8. 뒤집은 소수/in3.txt", "rt")

N = int(input())
numbers = list(map(str, input().split()))

def reverse(x):
    return x[::-1]

def isPrime(x):
    if x<2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

sosu = []
for num in numbers:
    n = int(reverse(num))
    if isPrime(n):
        sosu.append(n)

print(*sosu, sep=" ")

# 1은 소수 아님
# 7번 isPrime을 이용해야 3,4,5 test 가능할듯, 너무 느림