import os


def ttt():

    place =     [["","",""],
                 ["","",""],
                 ["","",""]]
    line = "---------------------------------"
    
    flag = True #순서 배정

    while True:
        
        print(place[0][0]+"\t|\t"+place[0][1]+"\t|\t"+place[0][2])
        print(line)
        print(place[1][0]+"\t|\t"+place[1][1]+"\t|\t"+place[1][2])
        print(line)
        print(place[2][0]+"\t|\t"+place[2][1]+"\t|\t"+place[2][2])
        if flag:
            a,b = map(int, input("플레이어 1 입력:").split())
            place[a][b] = "O"
            flag = False # 값 입력 후 2번 사용자 차례로 변경
        else:
            flag = True # 값 입력 후 1번 사용자 차례로 변경
            a,b = map(int, input("플레이어 2 입력:").split())
            place[a][b] = "X"

        os.system("cls")
   
        # win_player_1 = (place[0][0],[0][1],[0][2] = "O"
        #                 place[1][0],[1][1],[1][2] = "O"
        #                 place[2][0],[2][1],[2][2] = "O"
        #                 place[0][0],[1][0],[2][0] = "O"
        #                 place[0][1],[1][1],[2][1] = "O"
        #                 place[0][2],[1][2],[2][2] = "O"
        #                 place[0][0],[1][1],[2][2] = "O"
        #                 place[0][2],[1][1],[2][0] = "O")

        # win_player_2 = (place[0][0],[0][1],[0][2] = "X"
        #                 place[1][0],[1][1],[1][2] = "X"
        #                 place[2][0],[2][1],[2][2] = "X"
        #                 place[0][0],[1][0],[2][0] = "X"
        #                 place[0][1],[1][1],[2][1] = "X"
        #                 place[0][2],[1][2],[2][2] = "X"
        #                 place[0][0],[1][1],[2][2] = "X"
        #                 place[0][2],[1][1],[2][0] = "X")

        # error_message = 1

        # if win_player_1:
        #     print("플레이어 1 승리")
        #     break

        # elif win_player_2:
        #     print("플레이어 2 승리")
        #     break

        # elif error_message:
        #     print("다시 입력해주세요.")

        # else:

        
    return

ttt()

    # 아무도 선택하지 않은 곳은 0번
    # 1번의 선택은 1번
    # 2번의 선택은 2번
    # 0번이 아닌 곳을 선택 시 다시 선택하라는 메세지 출력
    # 각 플레이어가 한 번씩 입력할 때 마다 값을 검증해서
    # 각 플레이어의 승리를 확인

    # to do
    # 1. 리스트의 번호를 0이 아닌 1부터 시작하게 하기
    # 2. 각 플레이어의 입력 값을 배열에 추가하기
    # 3. 추가한 자리에는 새로운 값을 입력하지 못하게 하기(0일 경우일때만 입력 가능)
    # 3-1. 출력 "다른 자리에 놓아주세요."
    # 4. 각 플레이어의 승리 경우의 수 입력
    # 5. 승리 경우의 수 중 한가지 일치 시 "플레이어 n 승리" 출력