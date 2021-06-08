import sys
strings = sys.stdin.readline().strip()
n = len(strings)
i = 0
def encode(string):
    b_num = ''
    for i in range(len(string)-1,-1,-1):
        char = string[i]
        if "a"<= char <= "z":
            num = ord(char) - ord("a") + 1
            b_num = "{:06b}".format(num) + b_num
        elif "A" <= char <= "Z":
            num = ord(char) - ord("A") + 1 +26
            b_num = "{:06b}".format(num) + b_num
        elif "0" <= char <= "9":
            num = ord(char) - ord("0") + 1 + 26 + 26
            b_num = "{:06b}".format(num) + b_num
        else:
            b_num = "000000" + b_num
    d_num = 0
    e = 0
    for i in range(len(b_num)-1,-1,-1):
        d_num += int(b_num[i])*(2**e)
        e+=1
    return d_num

while(i < n):
    j =min((i+1) * 5, n)
    string = strings[i:j]
    en_num = encode(string)
    if j < n-1:
        print(en_num, end = " ")
    else:
        print(en_num)
    i += 5

