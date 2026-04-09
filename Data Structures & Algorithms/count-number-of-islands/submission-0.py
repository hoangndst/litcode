class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    self.dfs(grid, visited, i, j)

        return count


    def dfs(self, grid: List[List[str]], visited: List[List[str]], row: int, col: int):
        rows = len(grid)
        cols = len(grid[0])

        if row < 0 or col < 0 or row >= rows or col >= cols:
            return
        
        if grid[row][col] == "0" or visited[row][col] == 1:
            return
        
        visited[row][col] = 1

        moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for r, c in moves:
            self.dfs(grid, visited, row + r, col + c)