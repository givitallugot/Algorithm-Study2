def solution(citations):
    answer = 0
    htemp_list = list()
    citations.sort()
    
    n = len(citations)
    i = 0
    j = len(citations)-1
    
    while i <= j:
        mid = (i+j)//2
        htemp = citations[mid]
        if n-mid >= htemp:
            htemp_list.append(htemp)
            i = mid+1
            mid = (i+j)//2
        else:
            j = mid-1
            mid = (i+j)//2
            
    answer = max(htemp_list)
    return answer

## 처음에 이진정렬로 citations 내에 h index가 있다고 생각했으나, 아래 위키백과를 참고하여 hindex의 개념을 다시 확인
## https://en.wikipedia.org/wiki/H-index 
## 나머지 논문이 h번 이하 인용되었다는 조건은 사실 필요 없음 (hindex의 개념과 상관 없음)

def solution(citations):
    answer = 0
    htemp_list = list()
    citations.sort()
    
    n = len(citations)

    for h in range(n,0,-1):
        if citations[n-h] >= h:
            answer = h
            break
            
    return answer
