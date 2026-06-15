def gcd(a,b):
  while b!=0:
    a, b = b, a%b
  return a

T = int(input())
tc = []
for i in range(T):
  tc.append(input().split(" "))

for i in tc:
  s = 0
  for j in range(1,int(i[0])+1):
    A = int(i[1])+j + int(i[2])
    C = int(i[3])+j + int(i[4])
    s += gcd(A, C)
    s = s % 998244353
  print(s)
    
    
