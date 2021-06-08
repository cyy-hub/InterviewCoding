class Solution(object):

    def longestIncreasingPath_cyy(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            if dp[i][j]:
                return dp[i][j]
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0<= r < m and 0 <= c < n  and matrix[r][c] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(r,c))  # 下一层的最大深度
            dp[i][j] += 1  # 本层的深度在下层深度的基础上+1
            return dp[i][j]
            

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # dp[i][j] 开始的最长路径
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res,dfs(i,j))
        print(dp)
        return res
matrix1 = [[9,9,4],[6,6,8],[2,1,1]]
matrix2 = [[3,4,5],[3,2,6],[2,2,1]] 
matrix3 = [[1,2]]
so = Solution()

print(so.longestIncreasingPath_cyy(matrix3))


