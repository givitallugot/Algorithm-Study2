import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/2. 쇠막대기/in5.txt')

sticks = str(input())
stack = []
cnt = 0
i = 0
while i < len(sticks):
    if sticks[i:i+2] == '()':
        cnt += len(stack)
        i += 2
    elif sticks[i] == '(':
        # cnt += 1
        i += 1
        stack.append('(')
    elif sticks[i] == ')':
        cnt += 1
        stack.pop()
        i += 1


print(cnt)