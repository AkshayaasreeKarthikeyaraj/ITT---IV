def get_divisors(num):
    divisors = set()
    i = 2
    while i * i <= num:
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
        i += 1
    if num >= 2:
        divisors.add(num)
    return divisors

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    
    valid_k = get_divisors(N - 1)
    for K in get_divisors(N):
        X = N
        while X % K == 0:
            X //= K

        if X % K == 1:
            valid_k.add(K)
            
    print(len(valid_k))

if __name__ == '__main__':
    solve()
