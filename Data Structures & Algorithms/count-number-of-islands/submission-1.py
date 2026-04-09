class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(row: int, col: int):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if visited[row][col] == 1 or grid[row][col] == "0":
                return
            visited[row][col] = 1
            for r, c in moves:
                dfs(row + r, col + c)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    dfs(i, j)
    
        return count
