n = 10000
res = []
import pdb

def is_inver(num1,num2):
    num1_inver,e=0,10
    while(num1):
        num1_inver = num1_inver * e + num1%10
        num1 = num1//10
    if num1_inver == num2:
        return True
    else:
        return False

for i in range(1,n//4+1):
    if is_inver(i,i*4):
        res.append([i,i*4])
print(len(res))
print(res)