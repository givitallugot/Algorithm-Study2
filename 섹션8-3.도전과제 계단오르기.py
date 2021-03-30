# Top-Down 방식, DFS()를 이용


def DFS(len):
    if dy[len] > 0: # cut edge, 즉 메모이제이션 (이게 바로 다이나믹, 이를 사용하지 않으면 그냥 재귀)
        return dy[len]
    if len == 1 or len == 2:
        return len # 1층일 때 오르는 방법은 1개(1), 2층일 때 오르는 방법은 2개(2, 1+1)
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


if __name__ == "__main__":
    n = 7
    dy = [0]*(n+1)
    print(DFS(n))