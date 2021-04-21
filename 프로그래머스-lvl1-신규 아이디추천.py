import re

def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    s_to_del = '~!@#$%^&*()=+[{]}:?,<>/'
    for s in s_to_del:
        new_id = new_id.replace(s, '')
    
    # 3단계
    new_id = re.sub('(([.])\\2{1,})', '.', new_id) # 연속된 . 삭제
    
    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if new_id == '':
        new_id = "a"
    
    # 6,7단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = new_id.rstrip('.')
    elif len(new_id) <= 2:
        ns = new_id[-1]
        nl = 3-len(new_id)
        new_id += ns*nl # ns를 nl번 반복
            
    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))