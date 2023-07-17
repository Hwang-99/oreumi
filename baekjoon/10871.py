N,X = map(int,input().split())
A = list(map(int,input().split())) 
result = [] 

for i in range(len(A)): 
  if A[i] < X: 
    result.append(A[i]) 

print(*result)