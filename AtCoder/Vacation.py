N = int(input())
hap = []
for i in range(N):
    a = list(map(int, input().split()))
    hap.append(a)

dp = [[0] * len(hap[0]) for _ in range(N)]

for j in range(len(hap[0])):
    dp[0][j] = hap[0][j]

for i in range(1, N):
    for j in range(len(hap[i])):
        max_prev = -float('inf')
        for k in range(len(hap[i-1])):
            if j != k:
                if dp[i-1][k] > max_prev:
                    max_prev = dp[i-1][k]

        dp[i][j] = hap[i][j] + max_prev

print(max(dp[N-1]))
