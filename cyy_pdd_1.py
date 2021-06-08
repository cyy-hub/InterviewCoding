import sys 
n = int(sys.stdin.readline().strip())
def action(n):
    res = []
    for i in range(n):
        res.append(["0"] * n)
    mizi = n // 2
    if n % 2 == 1:
        mizi +=1
    for i in range(mizi, n-1):
        for j in range(n-1-i):
            res[j][i] = "1"
            res[n-1-j][n-1-i] = "5"
    if n % 2 == 1:
        mizi -= 1
    for i in range(1,mizi):
        for j in range(i):
            res[j][i] = "2"
            res[n-1-j][n-1-i] = "6"
    mizi = n // 2

    for j in range(1,mizi):
        for i in range(j):
            res[j][i] = "3"
            res[n-1-j][n-1-i] = "7"
    if n%2 ==1:
        mizi +=1
    for j in range(mizi,n-1):
        for i in range(n-1-j):
            res[j][i] = "4"
            res[n-1-j][n-1-i] = "8"
    for val in res:
        print(" ".join(val))
action(n)