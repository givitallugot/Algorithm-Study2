# 음료수 얼려 먹기

ice = [list(map(int, list(input()))) for i in range(4)]

# 00110
# 00011
# 11111
# 00000

def DFS(r, c, visited):
    if r < 0 or r > 3 or c < 0 or c > 4:
        return
    if ice[r][c] == 1:
        return
    if visited[r][c] == 0:
        visited[r][c] = 1
        DFS(r-1, c, visited)
        DFS(r+1, c, visited)
        DFS(r, c+1, visited)
        DFS(r, c-1, visited)
        return True

if __name__ == "__main__":
    visited = [[0]*5 for i in range(4)]
    cnt = 0

    for r in range(4):
        for c in range(5):
            if ice[r][c] == 0:
                if DFS(r,c,visited) == True: # 처음 0인 부분부터 시작할 것
                    cnt += 1
    print(cnt)

