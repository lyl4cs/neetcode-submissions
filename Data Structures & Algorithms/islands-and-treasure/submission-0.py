class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        q = collections.deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        def levels(r,c, distance):
            if (0 <= r < rows and 0 <= c < cols and grid[r][c] == 2147483647):
                grid[r][c] = distance
                q.append((r,c)) 
            
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                distance = grid[row][col] + 1
                levels(row + 1,col,distance)
                levels(row - 1,col,distance)
                levels(row,col + 1,distance)
                levels(row,col - 1,distance)


