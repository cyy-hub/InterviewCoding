import sys 
line = sys.stdin.readline().strip().split(" ")
n,m,k = int(line[0]),int(line[1]),int(line[2])
arr = []
for i in range(n):
    line = sys.stdin.readline().strip()
    val = list(map(int,line.split(" ")))
    arr.append(val)
arr.sort(key = lambda x:(-x[2],x[0]))
curr_w=0
curr_p = 0
for i in range(n):
    curr_w += arr[i][1]
    curr_p += arr[i][0]
    if curr_w< m and curr_p< k:
        continue
    else:
        print(i+1)
        break

