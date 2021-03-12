import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 7/10. 미로탐색/in1.txt')

def DFS(x,y):
    global cnt
    global dx, dy

    if (x==6) and (y==6):
        cnt = cnt + 1
    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1<tx<7 and -1<ty<7 and (board[tx][ty] == 0):
                board[tx][ty] = 1
                DFS(tx,ty)
                board[tx][ty] = 0

if __name__ == '__main__':
    cnt = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    board = [list(map(int, input().split())) for _ in range(7)]
    board[0][0] = 1
    
    DFS(0, 0)
    print(cnt)