#coding=utf-8
import sys 
str = input()
#print(str)
# print('Hello,World!')
def str2int(str):
    str = str.strip()
    if not str:
        return 0
    res, i, sign = 0,1,1
    int_max,int_min,bndry = 2**31-1, -2**31,2**31//10
    if str[0] == "-": 
        sign = -1
    elif str[0] != "+":
        i =0
    for c in str[i:]:
        if not "0" <= c <="9":
            return "It is not a valid sting!"
        if res>bndry or (res==bndry and c>"7"):
            return int_max() if sign==1 else int_min
        res = 10 * res + ord(c)-ord("0")
    return sign * res
print(str2int(str))
        
        
        
        
    
        