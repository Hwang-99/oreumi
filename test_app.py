def app():

    menu = -1
    
    while True:
        print("1. 구구단")
        print("2. 두수덧셈")
        print("3. 팩토리얼")
        print("4. 종료")
        menu = int(input("메뉴를 선택해주세요. :"))
        if menu == 1:
            gugu = int(input("몇 단? :"))
            for i in range(1, 10):
                    print("{} * {} = {}".format(gugu, i, gugu * i))
        elif menu == 2:
            a, b = map(int,input("두 수 입력 :").split())
            print(a + b)        
        elif menu == 3:
            a = int(input("팩토리얼을 구할 숫자 입력 : "))
            result = 1
            for item in range(1, a+1, 1):
                result *= item      
            print(result)
        elif menu == 4:
            print("프로그램 종료")
            break
        else:
            print("숫자 범위 내에서 입력하세요.")
            
    
        



    return



app()

'''
메뉴에서 int값을 입력받고
그에 대응하는 값에 대한 기능을 실행한다.
기능 실행 후 원래 메뉴로 돌아와서 출력
종료값 입력 시 break
'''