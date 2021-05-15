import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n):
    answer = 0
    
    n3 = convert(n, 3)
    answer = int(n3[::-1],3)
    
    return answer