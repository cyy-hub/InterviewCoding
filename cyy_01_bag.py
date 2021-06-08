# w = [2, 2, 3, 1, 5, 2] 
# v = [2, 3, 1, 5, 4, 3]
# def bag(w,v,W):
#     dp=[[0 for j in range(W+1)] for i in range(len(v)+1)]
#     # print(dp)
#     for i in range(1, len(v)+1):
#         for j in range(1, W+1):
#             if j-w[i-1]>=0:    # 第i个物品的重量
#                 dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
#             else:
#                 dp[i][j]=dp[i-1][j]
#     return dp[-1][-1]
# res=bag(w,v,10)
# print(res)
    
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        print(nums_sum)
        if nums_sum % 2:
            return False
        W = nums_sum // 2
        print(W)
        dp = [[False for j in range(W+1)] for i in range(len(nums)+1)]
        # print(dp)
        for i in range(len(nums)+1):
            dp[i][0] = True
        for i in range(1,len(nums)+1):
            for j in range(1,W+1):
                if j-nums[i-1]>-1:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
so = Solution()
print(so.canPartition([1,5,11,5]))
