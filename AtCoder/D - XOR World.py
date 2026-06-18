def xor_n(n):
    rem = n % 4
    if rem == 0:
        return n
    elif rem == 1:
        return 1
    elif rem == 2:
        return n + 1
    else:
        return 0

a, b = map(int, input().split())

res = xor_n(b) ^ xor_nn(a - 1)

print(res)
