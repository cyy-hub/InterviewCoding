import sys
line = sys.stdin.readline().strip().split(" ")
n, m = int(line[0]), int(line[1])
arr = []
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split(" ")))
    arr.append(values)
# 统计岛屿数量
res = 0
cout = 0
def dfs(r,c):
    count += 1
    arr[r][c] = 0
    for x,y in [r+1,c],(r-1,c),(r,c+1),(r,c-1)]:
        if 0<= x < n and 0<=y< m and arr[x][y] == 1:
            dfs(x,y)
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            count = 0
            dfs(i,j)
            res = max(res, count)
print(res)
