import sys
sys.stdin = open('C:/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 3/8. 곳감/in5.txt')

N = int(input())
gam = []

for _ in range(N):
    gam.append(list(map(int, input().split())))

M = int(input())

for _ in range(M):
    i, lr, loc = map(int, input().split()) # 열, 왼쪽/오른쪽, 회전명령개수
    loc = loc % N # 회전명령개수가 N보다 큰 경우
    if lr == 0: # 왼쪽
        temp = gam[i-1][loc:]
        temp.extend(gam[i-1][:loc])
        gam[i-1] = temp
    
    elif lr == 1: # 오른쪽
        temp =  gam[i-1][N-loc:]
        temp.extend(gam[i-1][:N-loc])
        gam[i-1] = temp


cnt = 0
for i in range(N//2+1):
    cnt += sum(gam[i][i:N-i])
    cnt += sum(gam[N-i-1][i:N-i])
cnt -= gam[N//2][N//2] # 두 번 더해진 맨 가운데 한 번 제외

print(cnt)
