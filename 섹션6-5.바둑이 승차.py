import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/5. 바둑이 승차/in2.txt')

# 탐욕알고리즘이라서 안됨, 부분집합 문제로 풀어야함
def DFS(i, sum):
    if i == N:
        print(sum)
        return
    else:
        print(i, sum)
        if sum + badk[i] <= C:
            sum += badk[i]
            DFS(i+1, sum)
        else:
            DFS(i+1, sum)

if __name__ == "__main__":
    C, N = map(int, input().split())
    badk = []
    for _ in range(N):
        badk.append(int(input()))
    badk.sort(reverse=True)
    DFS(0, 0)

# 부분집합 문제, Cut Edge
# 지금까지 부분집합에 들어간 값을 tsum에 두고, 들어가지 않은 합을 total - tsum이라고 할 때, 
# (현재까지의) sum + (total - tsum)이 result(현재까지 가장 큰 값)보다 작으면 굳이 내려갈 필요 없음, 가지치기

