import sys
import time
starttime = time.time()

sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/9. 봉우리/in5.txt')

N = int(input())
maps = [[0]*(N+2)]

for i in range(N):
    maps.append([0] + list(map(int, input().split())) + [0])
maps.append([0]*(N+2))

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):

        d = (maps[i][j] > maps[i-1][j]) # down
        u = (maps[i][j] > maps[i+1][j]) # up
        l = (maps[i][j] > maps[i][j-1]) # left
        r = (maps[i][j] > maps[i][j+1]) # right

        if d & u & l & r:
            cnt += 1

print(cnt)

endtime = time.time()
print('걸린 시간: ', endtime - starttime) 