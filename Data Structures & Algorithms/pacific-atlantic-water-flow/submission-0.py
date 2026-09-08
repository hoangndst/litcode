class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row = r + dr
                col = c + dc
                if (
                    0 <= row < rows
                    and 0 <= col < cols
                    and (row, col) not in visited
                    and heights[row][col] >= heights[r][c]
                ):
                    dfs(row, col, visited)

        for row in range(rows):
            dfs(row, 0, pac)
            dfs(row, cols - 1, atl)
        
        for col in range(cols):
            dfs(0, col, pac)
            dfs(rows - 1, col, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
        


