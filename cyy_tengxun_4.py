import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
n, m= values[0], values[1]

arr = []
for i in range(m):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    arr.append(values)

mat = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    row, clo = arr[i][0],arr[i][1]
    mat[row-1][clo-1] = 1

has = {}
# print("-"*5,mat)
for i in range(n):
    num_sum =sum(mat[i])
    for a in range(n):
        num_sum += mat[a][i]
    if num_sum == 1:
        for j in range(n):
            if mat[i][j] !=0 or mat[j][i]!=0:
                if has.get(j+1):
                    has[j+1].append(i+1)
                else:
                    has[j+1]=[i+1]
res = 0
print(has)
for lis in has.values():
    res+= len(lis)*(len(lis)-1)//2
print(res)    