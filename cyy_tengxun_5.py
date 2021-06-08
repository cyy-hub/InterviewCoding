import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
n, m, k = values[0], values[1], values[2]

arr = []
for i in range(m):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    arr.append(values)

for i in range(k):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    values.append(0)
    arr.append(values)
    

