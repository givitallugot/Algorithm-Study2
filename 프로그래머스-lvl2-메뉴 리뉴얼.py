from itertools import combinations

def solution(orders, course):
    answer = []

    for num in course:
        candidate = []
        candidict = dict()
        for order in orders:
            orderl = list(order)
            if len(orderl) >= num:
                candidate.extend(map(list,combinations(orderl, num)))
        
        for c in candidate:
            c.sort() # 알파벳 순서로
            c = ''.join(c)

            if c in candidict.keys():
                candidict[c] += 1
            else:
                candidict[c] = 1
        
        if len(candidict) != 0:
            maxval = max(list(candidict.values()))
            if maxval > 1:
                answer.extend([k for k,v in candidict.items() if v == maxval])
    
    answer.sort()
    return answer