import sys
import numpy as np
sys.stdin = open("C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 2/4. 대표값/in1.txt", "rt")

N = int(input())
numbers = list(map(int, input().split()))
m = int(round(np.mean(numbers)))
mumbers = [abs(numbers[i] - m) for i in range(N)]
id = list(range(1, N+1))

diff_dict = {id[i] : mumbers[i] for i in range(N)}
sorted_diff_dict = sorted(diff_dict.items(), reverse=False, key=lambda item: item[1]) 
# key가 아닌 value를 이용한 오름차순, 동점이면 알아서 id(학번) 순으로 정렬

print(m, sorted_diff_dict[0][0])

# 강의 꼭 듣기!*