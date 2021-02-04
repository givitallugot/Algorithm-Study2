import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/4. 두 리스트 합치기/in1.txt')

_ = input()
num1 = list(map(int, input().split()))
_ = input()
num2 = list(map(int, input().split()))

num1.extend(num2)
num1.sort()
print(num1)

# 이렇게 간단하게 할 수 있지만, 복잡하게 하는 방법?