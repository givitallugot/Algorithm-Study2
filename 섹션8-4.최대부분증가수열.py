# arr[i] 항이 증가수열의 마지막 항이라고 생각할 때, 그 경우의 수를
# arr[i-1]부터 arr[1]까지 항이 마지막 항이라고 생각했을 때 적은 메모이제이션을 이용해서 구함.
# 하나씩 볼 때 뒤에 수열은 볼 필요 없음

# arr[i]가 증가수열의 마지막 항일 때, 가장 긴 길이를 넣음

import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/4. 최대부분증가수열/in5.txt')

N = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy = [0]*(N+1)

dy[1] = 1
res = 0

for i in range(2, N+1):
    mxdy = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i]:
            if dy[j] > mxdy:
                mxdy = dy[j]
    dy[i] = mxdy+1
    if dy[i] > res:
        res = dy[i]

print(res)




# dy = [0]*(n+2)
# dy[1] = 1
# dy[2] = 2

# for i in range(3, n+2):
#     dy[i] = dy[i-1] + dy[i-2]

# print(dy[n+1])

