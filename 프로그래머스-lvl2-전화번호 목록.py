def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    return answer


# 아래 코드는 효율성 테스트를 통과하지 못함
def solution(phone_book):
    answer = True
    
    for number in phone_book:
        for phone in phone_book:
            if (number == phone[0:len(number)]) and (number != phone):
                answer = False
                return answer
        
    return answer

