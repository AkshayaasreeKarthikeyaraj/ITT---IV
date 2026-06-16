N, M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

i = 0
j = 0
count = 0

while j < M and i < N:

  if 2*A[i] >= B[j]:
    count += 1 
    i += 1
    j += 1
     
  elif 2*A[i] < B[j]:
    i += 1
    
  else:
    j += 1

print(count)
    
    
