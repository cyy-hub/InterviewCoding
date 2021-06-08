import sys
line = sys.stdin.readline().strip().split(" ")
m, n = int(line[0]), int(line[1])
res = []
for i in range(m):
    res.append([])
    for j in range(1,n+1):
        res[-1].append(j)
print(res)
    