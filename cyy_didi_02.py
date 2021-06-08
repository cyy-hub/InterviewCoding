import sys
line = sys.stdin.readline().strip().split(" ")
n,m = int(line[0]),int(line[1])
arr = []
for i in range(m):
    line = sys.stdin.readline().strip()
    arr.append(list(map(int, line.split(" "))))
line = sys.stdin.readline().strip().split(" ")
s,e, t = int(line[0]),int(line[1]),line[2]
inf = float("INF")
graph = [[inf] * n for i in range(n)]
for i in range(n):
    graph[arr[i][0]-1][arr[i][1]-1] = arr[i][2]
path = [[-1] * n for i in range(n)]
def back_path(path, i,j):
    while(-1 != path[i][j]):
        back_path(path,i,path[i][j])
        back_path(path,path[i][j],j)
        print(path[i][j])
        return 
    return 
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] +graph[k][j]:
                graph[i][j] = graph[i][k] +graph[k][j]
                path[i][j] = k

back_path(path,s-1,e-1)