# import sys
# line = sys.stdin.readline().strip().split(" ")
# n, m = int(line[0]), int(line[1])
# w, v = [], []
# for i in range(n):
#     line = sys.stdin.readline().strip()
#     val = list(map(int, line.split()))
#     w.append(val[0])
#     v.append(val[1])
w = [2, 2, 3, 1, 5, 2] 
v = [2, 3, 1, 5, 4, 3]
def bag(w,v,W):
    dp=[[0 for j in range(W+1)] for i in range(len(v)+1)]
    for i in range(1, len(v)+1):
        for j in range(1, W+1):
            if 0<= j-w[i-1]<= W:    # 第i个物品的重量
                # print(i,j)
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]
res = bag(w,v,10)
print(res)