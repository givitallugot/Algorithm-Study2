import sys
import numpy as np
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/6. 자릿수의 합/in5.txt", "rt")

N = int(input())
numbers = list(map(str, input().split()))

def digit_sum(x):
    sm = sum(map(int, list(x)))
    return sm

smlist = []
for i in range(N):
    sm = digit_sum(numbers[i])
    smlist.append(sm)

k = np.argmax(smlist)
print(int(numbers[k]))

# 꼭 숫자로 처리해야되나? 강의 듣기
# list를 이용하면 split를 character별로 가능