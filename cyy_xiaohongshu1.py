import sys 
string = sys.stdin.readline().strip().split(" ")
res = []
for char in string:
    if len(char) > 1 or "0" <= char <= "9":
        res.append(int(char))
    elif char == "+":
        if res == []:
            res.append(0)
        elif len(res) == 1:
            res.append(res[-1])
        else:
            res.append(res[-1]+res[-2])
    elif char == "C":
        if res != []:
            res.pop()
    elif char == "-":
        if len(res) >= 2:
            res.append(abs(res[-1]-res[-2]))
        elif res == []:
            res.append(0)
        else:
            res.append(res[-1])
    elif char == "T":
        if res != []:
            res.append(res[-1]*3)
        else:
            res.append(0)
print(sum(res))
