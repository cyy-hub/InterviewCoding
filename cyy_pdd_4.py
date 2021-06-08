import sys
line = sys.stdin.readline().strip().split(" ")
n, m = int(line[0]), int(line[1])
fea = []
for i in range(m):
    line = sys.stdin.readline().strip()
    fea.append(int(line))
res = 0
for val in fea:
    beichushu = n
    while(beichushu >= 1):
        if beichushu % val == 0:
            res += beichushu // val
            print(val,beichushu,res)
            break
        beichushu -= 1
print(res)
