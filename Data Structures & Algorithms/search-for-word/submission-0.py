class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        found = False
        visited = set()

        def dfs(r,c,k):
            nonlocal found
            if k == len(word):
                found = True
                return
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[k] and (r,c) not in visited:
                visited.add((r,c))
                dfs(r+1,c,k+1)
                dfs(r-1,c,k+1)
                dfs(r,c+1,k+1)
                dfs(r,c-1,k+1)
                visited.remove((r,c))
       
            
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    dfs(r,c,0)
        
        return found
