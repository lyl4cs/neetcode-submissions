class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #first check if its in bounds and then check if its a 1 not visited
        rows, cols = len(grid),len(grid[0])
        visited = set()
        islands = 0

        def dfs(r,c):
            if (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r,c) not in visited):
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        
        return islands
