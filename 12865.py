import sys
n, k = map(int, sys.stdin.readline().split())
weight = [0]*(n+1)
values = [0]*(n+1)
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    weight[i+1] = w
    values[i+1] = v
# dp = [0]*(k+1)
# for i in range(1, n+1):
#    for j in range(k, 0, -1):
#        if weight[i] <= j:
#            dp[j] = max(dp[j], dp[j-weight[i]] + values[i])
#print(dp[k])

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if weight[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + values[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])