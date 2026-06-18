N = int(input())
rating =list(map(int,input().split()))

val = set()
count = 0

for i in rating:
  if i <= 399:
    val.add("gray")
  elif i <= 799:
    val.add("brown")
  elif i <= 1199:
    val.add("green")
  elif i <= 1599:
    val.add("cyab")
  elif i <= 1999:
    val.add("blue")
  elif i <= 2399:
    val.add("yellow")
  elif i <= 2799:
    val.add("orange")
  elif i <= 3199:
    val.add("red")
  else:
    count += 1
    
max_r = len(val)
min_r = len(val)


if count > 0:
  max_r += count
  
print(min_r," ",max_r)
