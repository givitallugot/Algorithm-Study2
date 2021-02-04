import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 4/3. 뮤직비디오/in5.txt')

N, M = map(int, input().split())
song = list(map(int, input().split()))

start = max(sum(song)//M, max(song))
for ms in range(start, start*2):
    dvd = 0
    l = 0
    for i in range(N):
        if dvd + song[i] <= ms:
            dvd += song[i]
        elif dvd + song[i] > ms:
            dvd = song[i]
            l += 1

    if ((l == M-1) & (dvd <= ms)) or ((l == M) & (dvd == ms)):
        print(ms)
        break
