# 플로이드와샬 알고리즘 필요
# 대신 최단/최대 거리 업데이트 대신 -1, 0, 1 정도만

def solution(n, results):
    answer = 0
    
    fwtable = [[0]*n for i in range(n)]
    
    for [win, lose] in results:
        fwtable[win-1][lose-1] = 1
        fwtable[lose-1][win-1] = -1
        
    for k in range(n):                  # 1. 모든 노드를 중간점(경로)로 가정하며
        for i in range(n):              # 2. 점수판을 순회
            for j in range(n):          # 3. 만약 i가 k에 이겼고, k가 j에 이겼다면
                if fwtable[i][j] == 0:  # i는 j에게도 이김 (지는 것도 동일)
                    if fwtable[i][k] == 1 and fwtable[k][j] == 1:
                        fwtable[i][j] = 1
                    elif fwtable[i][k] == -1 and fwtable[k][j] == -1:
                        fwtable[i][j] = -1
    
    for winl in fwtable:
        if sum(list(map(abs, winl))) == n-1:
            answer += 1
            
    return answer


# 시간 초과
def solution(n, results):
    answer = 0
    
    l = list(range(1,n+1))
    result_dict = {1:l.copy(), 2:l.copy(), 3:l.copy(), 4:l.copy(), 5:l.copy()}
    
    for result in results:
        win = result[0]
        lose = result[1]
        
        # 이긴 경우
        result_dict[win].pop(-1) # 맨 뒤에서 빼기
        
        # 진 경우
        atleast = result_dict[win][0]
        result_dict[lose].pop(0) # (일단) 맨 앞에서 빼기
        
        # 플러스 이긴 사람의 맨 앞자리 빼고 그만큼까진 없애야함
        for j in range(1,atleast+1):
            if j in result_dict[lose]:
                result_dict[lose].remove(j)
    
    for val in result_dict.values():
        if len(val) == 1:
            answer += 1

    return answer

