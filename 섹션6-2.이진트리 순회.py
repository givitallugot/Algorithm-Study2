# 이진트리 순회 - 깊이우선탐색 (DFS)

# 부모, 왼쪽자식, 오른쪽자식 - 전위순회 
# 왼쪽자식, 부모, 오른쪽자식 - 중위순회
# 왼쪽자식, 오른쪽자식, 부모 - 후위순회

def DFS(v): # v = vertex = node
    if v > 7:
        return
    else:
        # print(v) # 출력 = 해야할 일

        # 1. 전위순위 위치 print(v)

        DFS(v*2) # 왼쪽 자식 노드 호출

        # 2. 중위순위 위치 print(v)

        DFS(v*2+1) # 오른쪽 자식 노드 호출

        # 3. 후위순위 위치 print(v)
        
if __name__ == "__main__":
    DFS(1)