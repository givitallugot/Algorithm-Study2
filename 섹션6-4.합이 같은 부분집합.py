import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/4. 합이 같은 부분집합/in5.txt')

def DFS(i):
    if i == N-1:
        sm = sum(list(map(lambda x: l[x[0]] if x[1] == 1 else 0, enumerate(ch))))
        if sm == sum(l) - sm:
            print("YES")
            sys.exit(0)
    else:
        i += 1
        ch[i] = 1
        DFS(i)
        ch[i] = 0
        DFS(i)

if __name__ == "__main__":
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    sets = []

    ch  = [0] * N
    i = 0
    DFS(i)

    ch  = [1] + [0] * (N-1)
    i = 0
    DFS(i)

    print('NO')

# 함수에 list는 넘어가는데 상수는 왜 안넘어가지?