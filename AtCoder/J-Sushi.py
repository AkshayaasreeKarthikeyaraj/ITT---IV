def solve():
    N = int(input())
    a = list(map(int, input().split()))
    c1 = a.count(1)
    c2 = a.count(2)
    c3 = a.count(3)

    dp = [[[0.0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for k in range(N + 1):         
        for j in range(N + 1 - k):  
            for i in range(N + 1 - j - k): 
                if i == 0 and j == 0 and k == 0:
                    continue
                
                total_sushi_dishes = i + j + k
                expected_steps = N / total_sushi_dishes
 
                if i > 0:
                    expected_steps += dp[i-1][j][k] * (i / total_sushi_dishes)
                if j > 0:
                    expected_steps += dp[i+1][j-1][k] * (j / total_sushi_dishes)
                if k > 0:
                    expected_steps += dp[i][j+1][k-1] * (k / total_sushi_dishes)
                    
                dp[i][j][k] = expected_steps
    print(f"{dp[c1][c2][c3]:.14f}")

if __name__ == '__main__':
    solve()
