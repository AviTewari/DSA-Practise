class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        m,n = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 or i>=m or j<0 or j>=n or grid[i][j] != "1":
                return
            else:
                grid[i][j] = "0"
                dfs(i,j-1)
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i-1,j)


        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    island+=1
                    dfs(i,j)
        return island