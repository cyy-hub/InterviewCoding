import pdb
import sys

line = sys.stdin.readline().strip().split(' ')
n,m = int(line[0]), int(line[1])
arr =[]
for i in range(n):
    line = sys.stdin.readline().strip().split(' ')
    arr.append([int(val) for val in line])
reward = []
for i in range(n):
    reward.append([arr[i][0]+2*arr[i][1],i+1])
reward = sorted(reward)
# print(reward)
# for i in range(m,0,-1):
#     print(reward[-i][1],end=" ")

res = []
while(len(res)<m):
    i = len(res)+1
    max_val = reward[-i][0]
    j = i
    tmp =[]
    while(reward[-j][0]==max_val):
        tmp.append(reward[-j][1])
        j+=1
    res.append(tmp)
print(res)