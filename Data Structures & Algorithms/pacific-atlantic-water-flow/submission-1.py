class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        pacific = []
        atlantic = []
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))

        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))

        def bfs(source, ocean):
            q = deque(source)

            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    row = r + dr
                    col = c + dc

                    if (
                        0 <= row < rows
                        and 0 <= col < cols
                        and not ocean[row][col]
                        and heights[row][col] >= heights[r][c]
                    ):
                        q.append((row, col))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])


        return res
