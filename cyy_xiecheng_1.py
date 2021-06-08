import sys
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

def find_b(string):
    char_dict = {}
    for char in string:
        if not char_dict.get(char):
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    small_num = len(string)+1
    for key in char_dict:
        small_num = min(small_num, char_dict[key])
    for key in char_dict:
        char_dict[key] /= small_num
    need_dit = {}
    match = 0
    b = ""
    for char in string:
        if not need_dit.get(char):
            need_dit[char] = 1
        else:
            need_dit[char] += 1
        if need_dit[char] == char_dict[char]:
            match +=1
        b+=char
        if match == len(char_dict):
            break
    return b
b1 = find_b(str1)
b2 = find_b(str2)
if b1 == b2:
    print(b1)
else:
    print("")
            


    