#!/usr/bin/env python3


# Number of Islands
# Depth First Search is used (Breadth First Search could also be used)
# Time complexity: O(rows x columns)
# Space complexity: O(rows x columns)


def find_num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0
    # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return

        grid[row][col] = 0
        # for dr, dc in directions:
        #     dfs(row + dr, col + dc)

        # This is for vertical and horizontal neighbors counting towards a
        # single group:
        # for i in range(-1, 1):
        #     for j in range(-1, 1):
        # This is when horizontal, vertical and diagonal neighbors count:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                dfs(row + i, col + j)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                num_islands += 1
                dfs(r, c)

    return num_islands


if __name__ == "__main__":
    pass

    matrix = [
        [1, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]

    num_islands = find_num_islands(matrix)
    print(num_islands)
