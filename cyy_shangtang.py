import sys
line="123 GoodoodGGoooddjfhjdGGooo3dkdggggGoood0123\n"
stack = []
l_stack=[]
l=0
res = 0
for char in line:
    if char in ["G","o","d"]:
        
        if char == "G":
            stack.append(char)
            g_index =len(stack)-1
            l_stack.append(l)
            l = 1
        elif l>0 and char =="o":
            stack.append(char)
            l+=1
        elif l>=3 and char == "d":
            print("-"*5)
            stack.append(char)
            res +=1
            stack.pop(g_index)
            stack.pop()
            stack.pop()
            stack.pop()
            onum=l-3
            l=l_stack.pop()+onum
    print(char,stack,l,l_stack)
print(res)
                
            
                
                
 