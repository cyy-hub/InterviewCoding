class Solution(object):
    def __init__(self):
        self.res = 0
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            # print(i,j, self.res)
            grid[i][j] = 2
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:  # 走四个方向，看会发生什么情况嘛
                if r < 0 or r >= m or c < 0 or c >= n:     # 往边界走了一格
                    print("bian",i,j,r,c)
                    self.res += 1
                if 0<= r < m and 0<= c < n and grid[r][c] == 0 : # 往水域走了一格
                    print("shui",i,j,r,c)
                    self.res +=1
                if 0<= r < m and 0<= c < n and grid[r][c] == 1:   
                    dfs(r,c)


        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for i in range(m):   # 要区别是走过的陆地不能走还是原本就是水域不能走
            for j in range(n):
                # print(i,j)
                if grid[i][j] == 1:
                    dfs(i,j)
        return self.res

grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
so = Solution()
print(so.islandPerimeter(grid))