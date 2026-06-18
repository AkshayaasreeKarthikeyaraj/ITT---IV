def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    P = [float(x) for x in input_data[1:]]
    
    dp = [0.0] * (N + 1)
    dp[0] = 1.0
    
    for p in P:
        for j in range(N, -1, -1):
            tail_prob = dp[j] * (1.0 - p)
            head_prob = dp[j - 1] * p if j > 0 else 0.0
            dp[j] = tail_prob + head_prob
            
    ans = 0.0
    for j in range((N // 2) + 1, N + 1):
        ans += dp[j]
        
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()
