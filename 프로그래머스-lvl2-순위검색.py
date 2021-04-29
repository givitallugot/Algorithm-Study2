# 틀린 코드

from collections import Counter

def solution(info, query):
    answer = []
    infol = [[] for i in range(5)]
    
    for i in info:
        l = list(i.split(' '))
        infol[0].append(l[0])
        infol[1].append(l[1])
        infol[2].append(l[2])
        infol[3].append(l[3])
        infol[4].append(l[4])
    
    option = []
    for q in query:
        option = list(q.split(' '))
        option.remove('and'); option.remove('and'); option.remove('and')
        idx = list()
        
        # 앞의 네 속성
        for i in range(4):
            if option[i] == '-': # 모두 가능
                idx.extend([0,1,2,3,4])
            else:
                idx.extend([ix for ix, il in enumerate(infol[i]) if il == option[i]])
            # append 쓰면 각 문제마다 조건 만족하는 info의 index로 나뉨
            # 어차피 counter 쓰니까 합치기
        
        # 코테 점수
        idx.extend([ix for ix, il in enumerate(infol[4]) if int(il) >= int(option[4])])
        
        idxdct = Counter(idx)
        # print(idxdct)
        answer.append(len([k for k,v in idxdct.items() if v == 5]))
        # print(answer)
        
    return answer