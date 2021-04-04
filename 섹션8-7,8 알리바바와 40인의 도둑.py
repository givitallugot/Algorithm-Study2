import sys
from collections import deque
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/7, 8. 알리바바와 40인의 도둑/in0.txt')

N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]
D = [[0]*N for _ in range(N)]
D[0][0] = R[0][0]

dx = [1, 0] # 행
dy = [0, 1] # 열

Q = deque()
Q.append((0,0))
L = 0

while Q:
    now = Q.popleft()
    if now == (N-1, N-1):
        break
    
    print(now)
    mn = 10; newx = 0; newy = 0
    for i in range(2):
        x = now[0] + dx[i]
        y = now[1] + dy[i]

        if x < N and y < N and R[x][y] < mn:
            mn = R[x][y]
            newx = x
            newy = y
    
    Q.append((newx, newy))
    D[newx][newy] = D[now[0]][now[1]] + mn

print(D[N-1][N-1])
print(D)

# 현재 위치에서 최선을 찾는 방법 (그리디 서치) != 현재 위치까지 오는 방법 중 가장 최선 (다이나믹)
# dy[i][j]는 0,0에서 i,j까지 가는데 드는 최소 비용


#### 올바른 풀이1 - Bottom up ####
import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/7, 8. 알리바바와 40인의 도둑/in0.txt')

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    dy[0][0] = arr[0][0]

    for i in range(n):
        # 위, 왼 가장자리 메우기
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]

    for i in range(1,n):
        for j in range(1,n):
            dy[i][j] = min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    
print(dy[n-1][n-1])



#### 올바른 풀이2 - Top down ####
import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 8/7, 8. 알리바바와 40인의 도둑/in5.txt')

def DFS(x,y):
    if dy[x][y] > 0: # 메모이제이션 이용, cut edge
        return dy[x][y] # 이미 기록된 값 return
    if x==0 and y==0: # 출발점일 때
        return arr[0][0] # 첫 번째 돌의 에너지 값
    else:
        if y == 0: # 맨 오른쪽일 때
            dy[x][y] = DFS(x-1, y) + arr[x][y] #  + 자기돌
        elif x == 0: # 맨 위일 때
            dy[x][y] = DFS(x, y-1) + arr[x][y] #  + 자기돌
        else:
            dy[x][y] = min(DFS(x-1,y), DFS(x,y-1)) + arr[x][y] # 바로 윗 돌 또는 왼쪽 돌 중 작은 값 + 현재 돌
        return dy[x][y]

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)] # 메모이제이션을 위해
    dy[0][0] = arr[0][0]

print(DFS(n-1, n-1))