import sys 
line = sys.stdin.readline().strip()
n = int(line[0])
arr = []
for i in range(n):
    line = sys.stdin.readline().strip()
    val = list(map(int,line.split(" ")))
    arr.append(val)

for i in range(n):
    for j in range(n):
        mum, tmp = 0,0
        for x,y in [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0<=x <n and 0<=y <n:
                num +=1
                tmp += arr[x][y]
        val= tmp /num
        if int(val) + 0.5 <= val:
            arr[i][j] = int(val)+1
        else:
            arr[i][j] = int(val)
for line in arr:
    res = " ".jion([str(val) for val in line])
    print(res)
        
                
