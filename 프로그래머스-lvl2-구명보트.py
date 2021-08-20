# 정확도 X

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    temp = 0
    for person in people:
        if temp + person <= limit:
            temp += person
        else:
            temp = person
            answer += 1
            
    answer += 1
    
    return answer

# 정확도 100 효율성 X

# 가장 큰 무게와 같이 탈 수 있을 법한 사람은 가장 작은 사람부터 찾아야할 것.
# 만약 가장 작은 사람도 같이 못타면 그냥 어쩔 수 없이 혼자가야 함 => 그래서 탐욕법이 가능함.

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    while people:
        boat = people.pop(0)
        answer += 1
        
        while people:
            if (boat + people[-1]) <= limit:
                boat += people.pop(-1)
            else:
                break

    
    return answer

# 
# 문제를 잘못 봄.. 2명씩 밖에 탈 수가 없다고 함.
# 간단한 문제라서 pop을 쓰는게 시간 복잡도에 영향.

# 가장 큰 무게와 같이 탈 수 있을 법한 사람은 가장 작은 사람부터 찾아야할 것.
# 만약 가장 작은 사람도 같이 못타면 그냥 어쩔 수 없이 혼자가야 함 => 그래서 탐욕법이 가능함.

# pop을 사용하면 통과를 할 수가 없음.

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    i = 0; j = len(people)-1
    while i <= j:
        
        if i == j:
            answer += 1
            break
            
        if people[i] + people[j] <= limit:
            j -= 1
        answer += 1
        i += 1
        
    
    return answer