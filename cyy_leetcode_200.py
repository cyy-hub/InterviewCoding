def num_island(grid):
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(i,j,m,n)
    return count 
def dfs(i,j,m,n):
    grid[i][j] = "0"
    for r,c in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
        if 0<= r< m and 0<= c< n and grid[r][c] == "1":
            dfs(r,c,m,n)
            
grid = [
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','1']
]
print(num_island(grid))


