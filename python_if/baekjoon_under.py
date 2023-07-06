N,X = map(int,input().split())
A = list(map(int,input().split())) #스페이스로 구분된 정수형 입력을 리스트화
result = [] #결과값을 담을 빈 리스트

for i in range(len(A)): #입력받은 A리스트 요소의 개수만큼 반복
  if i < X: #i가 0일때 A[0]의 값과 정수X를 비교 후 X보다 작을 시 실행
    result.append(A[i]) #저 위에 생성해놓은 결과값을 담을 리스트에 X와 비교된 놈을 추가

print(result[i], end = " ")
