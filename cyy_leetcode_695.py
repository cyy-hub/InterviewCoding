
class Solution(object):
    def __init__(self):
        self.res = 0
        self.mid_res = 0
    def max_aere_island(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        def dfs(i,j,m,n):
            self.mid_res += 1
            grid[i][j] = 0
            for r,c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= r < m and 0<= c < n and grid[r][c] == 1:
                    dfs(r, c, m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.mid_res = 0
                    dfs(i,j,m,n)
                    self.res = max(self.res, self.mid_res)
        return self.res



if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    so = Solution()
    print(so.max_aere_island(grid))
