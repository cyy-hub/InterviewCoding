# s1_hash = {}
# for char in s1:
#     if s1_hash.get(char):
#         s1_hash[char]+=1
#     else:
#         s1_hash[char]=1
# res_flag=False
# for char in s2:
#     if not s1_hash.get(char):
#         # print(False)
#         res_flage=True
#         break
#     else:
#         s1_hash[char]-=1
#         if s1_hash[char]==-1:
#              # print(False)
#             res_flage=True
#             break
# if res_flag:
#     print(0)
# else:
#     print(1)

# import sys
# num= int(sys.stdin.readline().strip())
num = 41
v=[0]*101 
p=[0] # 质数
e={}
for i in range(2,101):
    if v[i]==0:         
        v[i]=i
        p.append(i)
    for j in range(1,len(p)):
        if p[j]>v[i] or p[j]>100/i:
            break
        v[i*p[j]]=p[j]
for i in range(1,len(p)):
    p[i]+= p[i-1]
    e[p[i]] = True
res=0
for i in range(len(p)):
    if e.get(p[i]+num):
        if e[p[i]+num]:
            res+=1
print(v)
print("-"*50)
print(p)
print(res)


  