import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/5. 회의실 배정/in5.txt')

n = int(input())
room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

room = [[j,i] for [i,j] in room]
room.sort() # 종료 시간 기준으로 정렬

room = [[j,i] for [i,j] in room]

greed = [room[0]]
gl = 1

for meet in room[1:]:
    if greed[gl-1][1] <= meet[0]:
        gl += 1
        greed.append(meet)

print(gl)
        