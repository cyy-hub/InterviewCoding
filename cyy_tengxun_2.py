import sys 
n = int(sys.stdin.readline().strip())

# res2 = n*2**(n-1)
# print(res2)

def pow(b):
    res = 1
    base = 2
    while(b):
        if n & 1:
             res = res * base
        base = (base * base) 
        n >>= 1
    return 

