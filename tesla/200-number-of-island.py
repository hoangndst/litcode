# https://leetcode.com/problems/number-of-islands/
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    self.dfs(i, j, grid, visited)

        return count

    def dfs(self, r: int, c: int, grid: List[List[str]], visited: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if visited[r][c] == 1 or grid[r][c] == "0":
            return
        visited[r][c] = 1

        self.dfs(r - 1, c, grid, visited)
        self.dfs(r + 1, c, grid, visited)
        self.dfs(r, c - 1, grid, visited)
        self.dfs(r, c + 1, grid, visited)

        