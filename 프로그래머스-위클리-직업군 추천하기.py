import numpy as np

def solution(table, languages, preference):
    answer = ''
    table.sort()

    maxx = -1
    langpredict = {languages[i]:preference[i] for i in range(len(languages))}

    for t in table:
        t = t.split()
        summ = 0
        for i in range(5,0,-1):
            if t[5-i+1] in langpredict.keys():
                summ += i*langpredict[t[5-i+1]]

        if maxx < summ:
            maxx = summ
            answer = t[0]


    return answer