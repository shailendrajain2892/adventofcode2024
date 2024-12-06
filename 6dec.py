import os

def find_guard_init_pos(grid, m, n):
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "^":
                return i, j
    return -1, -1
def find_distinct_pos(grid):
    # print(grid)
    m, n = len(grid), len(grid[0])

    i, j  = find_guard_init_pos(grid, m, n)
    if i == -1 and j == -1:
        return 0

    grid[i][j] = "X"

    while i != 0 and j != 0 and i != m-1 and j != n-1:

        # move north
        while 0 <= i-1 < m and 0 <= j < n and grid[i-1][j] != "#":
            i, j = i-1, j
            grid[i][j] = "X"
        # move East
        while 0 <= i < m and 0 <= j+1 < n and grid[i][j+1] != "#":
            i, j = i, j+1
            grid[i][j] = "X"
        # move South
        while 0 <= i+1 < m and 0 <= j < n and grid[i+1][j] != "#":
            i, j = i+1, j
            grid[i][j] = "X"
        # move west
        while 0 <= i < m and 0 <= j-1 < n and grid[i][j-1] != "#":
            i, j = i, j-1
            grid[i][j] = "X"

    
    count=0
    for x in range(m):
        for y in range(n):
            if grid[x][y] == "X":
                count+=1
    return count

    
def main(grid=None):
    if not grid:
        grid = []
        file_path = os.path.join(os.path.dirname(__file__), 'data/6.txt')
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    grid.append(list(line))
    return find_distinct_pos(grid)

grid_data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
grid = [list(line) for line in grid_data.strip().split("\n")]

print(main())