import sys
sys.stdin = open('/Users/clue7/Desktop/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 5/3. 후위표기식 만들기/in3.txt')

def isPrior(s):
    # e의 우선순위가 더 높거나 같을때 TRUE
    if s in ['+', '-']:
        return True
    else:
        return False

exp = str(input())
result = []
stack = []
nlist = list(map(str, list(range(1,10))))

for e in exp:
    if e in nlist:
        result += e
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while stack[-1] != '(':
            tmp = stack.pop()
        if stack[-1] == '(':
            stack.pop() # '('를 삭제
    else:
        for i in range(len(stack)):
            if isPrior(stack[i]):
                result += stack.pop(i)
        stack.append(e)
    print(result, stack)

result = ''.join(result)
print(result)