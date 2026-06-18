def lucky(n):
    l = list(str(n))
    if len(l) != 4:
        return False
    s = 0
    while n != 0:
        s += n%10
        n = n//10
        
    if s%3 == 0 or s%5 == 0 or s%7 == 0:
        return True
    return False
    

n = int(input())
if lucky(n):
    print("Lucky Number")
else:
    print("Not Lucky Number")
