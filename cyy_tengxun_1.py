import sys
t = int(sys.stdin.readline().strip())

for i in range(t):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    a, b, c, d = values[0], values[1], values[2],values[3]
    res = (1/3*a*d**3 + 1/2*d**2 + b*d) - (1/3*a*c**3 + 1/2*c**2 + b*c)
    print("%.6f" % res)