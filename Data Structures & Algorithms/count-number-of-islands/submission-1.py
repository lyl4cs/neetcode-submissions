class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid:
            return 0

        # setting constraints and common variables we know we need
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] == "0" or (r,c) in visited):
                return None
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)




        # outer loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c) # add island count after running bfs and checking all
                    islands += 1
        return islands