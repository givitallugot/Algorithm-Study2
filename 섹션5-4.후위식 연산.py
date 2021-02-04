import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/4. 후위식 연산/in5.txt')

formula = input()
stack = []

for f in formula:
    if f.isdecimal():
        stack.append(f)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(str(eval(b+f+a)))

print(int(stack[0]))

