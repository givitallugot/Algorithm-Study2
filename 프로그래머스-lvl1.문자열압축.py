# 틀린 코드
from collections import Counter

def solution(s):
    answer = 1000
    
    for i in range(1,len(s)+1):
        scount = []
        cmin = 0
        
        ncut = int(len(s)/i) # 잘림
        for n in range(ncut+1):
            scount.append(s[i*n:i*(n+1)])
        scountdic = Counter(scount)
        print(scountdic)
        
        for k,v in scountdic.items():
            if v > 1:
                cmin += (len(k) + 1)
            elif k != '':
                cmin += len(k)
        
        if cmin < answer:
            answer = cmin
        
    return answer



# 수정 코드 짜보기