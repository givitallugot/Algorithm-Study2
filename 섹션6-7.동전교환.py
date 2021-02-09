import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/7. 동전교환/in5.txt')

def DFS(i, sum):
    if sum == M:
        print(i)
        sys.exit(0)
    elif sum > M:
        return
    else:
        for c in coin:
            DFS(i+1, sum + c)

if __name__ == '__main__':
    N = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)
    M = int(input())

    DFS(0, 0)

# 하나 틀림. 멈추지 말고 모두 돌아야함
# res로 기존보다 작은지 비교 + res보다 깊은 level로 들어가면 cut
# 중복 순열 문제와 비슷