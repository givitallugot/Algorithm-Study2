import sys
import time
starttime = time.time()

sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/11. 격자판 회문수/in5.txt')
pan = []

for _ in range(7):
    pan.append(list(map(int, input().split())))

cnt = 0

for i in range(7): # 동일 행에 있는 회문수 검사
    r1 = pan[i]; r2 = pan[i][::-1]
    cnt += sum([r1[0:5] == r2[2:7], r1[1:6] == r2[1:6], r1[2:7] == r2[0:5]])

for j in range(7): # 동일 열에 있는 회문수 검사
    c1 = [s[j] for s in pan]; c2 = [s[j] for s in pan][::-1]
    cnt += sum([c1[0:5] == c2[2:7], c1[1:6] == c2[1:6], c1[2:7] == c2[0:5]])

print(cnt)

endtime = time.time()
print('걸린 시간: ', endtime - starttime)
