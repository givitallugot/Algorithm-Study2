B = []

def check(b, t):
    # 0 (x, y)
    delx = b[0][0] - t[0][0]; dely = b[0][1] - t[0][1]
    newt = [(x+delx, y+dely) for (x,y) in t]
    if b == newt:
        return True

    # 90 (-y, x)
    newt = [(-y, x) for (x,y) in t]
    newt.sort()
    delx = b[0][0] - newt[0][0]; dely = b[0][1] - newt[0][1]
    newt = [(x+delx, y+dely) for (x,y) in newt]
    if b == newt:
        return True

    # 180 (-x, -y)
    newt = [(-x, -y) for (x,y) in t]
    newt.sort()
    delx = b[0][0] - newt[0][0]; dely = b[0][1] - newt[0][1]
    newt = [(x+delx, y+dely) for (x,y) in newt]
    if b == newt:
        return True

    # 270 (y, -x)
    newt = [(y, -x) for (x,y) in t]
    newt.sort()
    delx = b[0][0] - newt[0][0]; dely = b[0][1] - newt[0][1]
    newt = [(x+delx, y+dely) for (x,y) in newt]
    if b == newt:
        return True


def DFS(x, y, zero, one, N, board, shape):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        # B.append(shape)
        return False
    if board[x][y] == zero:
        shape.append((x,y))
        board[x][y] = one
        DFS(x-1, y, zero, one, N, board, shape)
        DFS(x, y-1, zero, one, N, board, shape)
        DFS(x+1, y, zero, one, N, board, shape)
        DFS(x, y+1, zero, one, N, board, shape)
        return shape
    return False


def solution(game_board, table):
    answer = 0
    N = len(game_board)
    Tdict = dict()

    for i in range(N):
        for j in range(N):
            # DFS 수행
            shape1 = DFS(i, j, 0, 1, N, game_board, [])
            shape2 = DFS(i, j, 1, 0, N, table, [])

            if shape1 != False:
                shape1.sort()
                B.append(shape1)

            if shape2 != False:
                shape2.sort()
                Tdict.setdefault(len(shape2), [])
                Tdict[len(shape2)].append(shape2)

    for b in B:
        nb = len(b)
        if (nb in Tdict.keys()) and len(Tdict[nb]) != 0:
            temp = Tdict[nb]
            for t in temp:
                # 함수 만들고 true 이면
                if check(b, t):
                    Tdict[nb].remove(t)
                    answer += nb
                    break

    return answer



