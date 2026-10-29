class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base case
        if not grid:
            return 0

        # setting constraints and common variables we know we need
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) 
                    and grid[r][c] == '1' and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))





        # outer loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c) # add island count after running bfs and checking all
                    islands += 1
        return islands