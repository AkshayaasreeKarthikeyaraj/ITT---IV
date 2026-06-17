n = int(input())
b = []
while n != 0:
    b.append(n%2)
    n = n//2
    
b.reverse()
num = 0
for i in b:
    num = num*10 + i
    
print(num)
