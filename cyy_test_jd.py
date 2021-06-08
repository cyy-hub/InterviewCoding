# N,M=110,120
# def huiwen(num):
#     l=len(str(num))
#     lis=[int(x) for x in str(num)]
#     for j in range(l//2):
#         if lis[j]!=lis[l-1-j]:
#             return False
#     return True
# def sushu(num):
#     if num>1:
#         for j in range(2,num):
#             if num%j==0:
#                 # print(num,j)
#                 return False
#     return True
# count=0

# # print(sushu(111),huiwen(111))
# for val in range(N,M):
#     if sushu(val) and huiwen(val):
#         #print(count)
#         count+=1
# print(count)

n=6
ser1="ABCDEE"
ser2="AEDCBB"

def longest(text1,text2):
    l1,l2=len(text1),len(text2)
    dp=[[0]*(l2+1) for _ in range(l1+1)]
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

con=longest(ser1,ser2)
if con/n<=0.5:
    print(con/n,"Yes")
else:
    print("No")