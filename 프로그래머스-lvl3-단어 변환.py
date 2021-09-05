def diffoneTF(word1, word2):
    diffcount = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diffcount += 1
        if diffcount > 1:
            return False
    return True

def solution(begin, target, words):
    answer = 0
    visited = [0]*len(words)
    words.sort()
        
    Q = []
    Q.append([0, begin])
    while Q:
        now = Q.pop(0)
        if now[1] == target:
            answer = now[0]
            break
                    
        for i in range(len(words)):
            if diffoneTF(now[1], words[i]) and (visited[i] == 0):
                visited[i] = 1
                Q.append([now[0]+1, words[i]])
        
        print(Q)
    
    return answer