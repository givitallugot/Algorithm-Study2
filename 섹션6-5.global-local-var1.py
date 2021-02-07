# 전역변수와 지역변수

def DFS1():
    # 지역변수인지 먼저 확인, 맞다면 지역변수로 인식, 아니라면 전역변수 공간에서 확인
    cnt = 3
    print(cnt) 

def DFS2():
    global cnt
    if cnt == 5:
        cnt = cnt + 1 # 에러, cnt = 을 지역변수로 생각
        # 따라서 gobal cnt를 추가하면, 왼쪽의 cnt를 전역변수로 생각하고 에러없이 실행
        print(cnt)

if __name__ == "__main__":
    # 전역변수
    cnt = 5 # 변수 생성 및 값 할당
    DFS1()
    DFS2()
    print(cnt)