import sys
import collections
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/8. 단어찾기/in5.txt')

N = int(input())
word = []
poem = []

for _ in range(N):
    word.append(input())
    
for _ in range(N-1):
    poem.append(input())

print(list(collections.Counter(word) - collections.Counter(poem))[0])