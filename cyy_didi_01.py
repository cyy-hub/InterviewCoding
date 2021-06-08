import sys 
t = int(sys.stdin.readline().strip())

def dfs(M,visited,i):
    for j in range(len(M)):
        if M[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(M, visited, j)

for j in range(t):
    line = sys.stdin.readline().strip().split(" ")
    n,m,k = int(line[0]), int(line[1]),int(line[2])
    arr = []
    for i in range(m):
        line = sys.stdin.readline().strip()
        arr.append(list(map(int, line.split(" "))))
    m = [[0]*n for __ in range(n)]
    for i in range(n):
        m[i][i] = 1
    for i in range(n):
        if arr[i][2] <= k:
            m[arr[i][0]-1][arr[i][1]-1] = 1
    visited = [0] * n
    count = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(m,visited,i)
            count +=1
    if count > 1:
        print("No")
    else:
        print("Yes")
    
    