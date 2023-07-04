global_var = 100

def my_func(global_var):

    # global global_var

    local_var = 50
    global_var += 50 # 일반적으로 값을 바꿀 수 없음
    print("전역 변수:", global_var)
    print("지역 변수:", local_var)

    return global_var

global_var = my_func(global_var)
print("전역 변수:", global_var)
# print("지역 변수:", local_var) # 지역 변수는 내부에서만 사용 가능

#전역 변수를 사용하는 경우는 특수한 경우