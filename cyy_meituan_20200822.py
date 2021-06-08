import pdb
import sys
t = int(sys.stdin.readline().strip())
def is_valiabel(string):
    has_min=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    has_big=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num_hash = ["0","1","2","3","4","5","6","7","8","9"]
    
    if not string:
        return "Wrong"
    else:
        # if (not 0<= ord(string[0])-ord("A")< 26) or (not 0<= ord(string[0])-ord("a")< 26):
        if string[0] not in has_big and string[0] not in has_min:
            return "Wrong"
        num_min, num_big, num_fig = 0,0,0
        for char in string:
            if char in has_min:
                num_min +=1
            elif char in has_big:
                num_big +=1
            elif char in num_hash:
                num_fig += 1
            else:
                # pdb.set_trace()
                return  "Wrong"
        # pdb.set_trace()
        # print(num_min,num_big,num_fig)
        if num_fig>0 and (num_min>0 or num_big>0):
            return "Accept"
        else:
            return "Wrong"

# is_valiabel("Hhhh666")
# strings=["Ooook","Hhhh666","ABCD","Meituan","6666"]
# for string in strings:
#     print(is_valiabel(string))

        
for i in range(t):
    string = sys.stdin.readline().strip()
    print(is_valiabel(string))