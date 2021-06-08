import pdb
import sys
x = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip().split(" ")
l, t, n = int(line[0]), int(line[1]), int(line[2])
line = sys.stdin.readline().strip()
a_list = list(map(int, line.split(" ")))
a_list.sort()
print(a_list)
res = n
cur_position = 0



# def dfs(cur_position, rest_time):
#     # print(cur_position, rest_time)
#     if cur_position >= x :
#         global res
#         if  cur_position in a_list:
#             res = min(res, rest_time+1)
#         else:
#             res = min(res, rest_time)
#         return 
#     if cur_position in a_list:
#         rest_time += 1
#     for val in range(l,t+1):
#         dfs(cur_position+val, rest_time)
#     if cur_position in a_list:
#         rest_time -= 1
# dfs(0,0)
# print(res)
