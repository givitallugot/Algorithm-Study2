import sys
sys.stdin = open('/Users/clue7/Desktop/코테스터디2/섹션 6/3. 부분집합 구하기/in1.txt')

N = int(input())

# 매우어렵.. 다시 풀어보기..
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
    