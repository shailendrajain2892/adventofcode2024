import os

def count_xmas(grid):
    directions = [
        (0, 1), #East
        (0, -1), #West
        (1, 0), #North
        (-1, 0), #Sout
        (1, 1), #ES
        (-1, -1), #WN
        (-1, 1), #NE
        (1, -1), #SW
    ]
    m, n = len(grid), len(grid[0])

    def find_xmas_dir(i, j, dx, dy):
        word = "XMAS"
        for k, char in enumerate(word):
            nx, ny = i + k*dx, j+ k*dy
            if not (0<= nx < m and 0 <= ny < n) or grid[nx][ny] != char:
                return False
        return True

    count=0
    for i in range(m):
        for j in range(n):
            for dx, dy in directions:
                if find_xmas_dir(i, j, dx, dy):
                    count+=1
    return count

def count_mas_patterns(grid):
    """
    Count the number of MAS patterns in X or + shapes in the grid.
    
    Args:
        grid (List[List[str]]): 2D grid representing the word search.
        
    Returns:
        int: The number of MAS patterns found.
    """
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Iterate over possible centers for the patterns
    for r in range(1, rows - 1):  # Avoid edges for center
        for c in range(1, cols - 1):  # Avoid edges for center
            if grid[r][c] == 'A':  # Center of the pattern must be 'A'
                if 0 <= r+1 < rows and 0 <= r-1 < rows and 0 <= c-1 < cols and 0 <= c+1 < cols:
                    # Check X-shaped pattern
                    if (
                        (grid[r-1][c-1] == 'M' and grid[r-1][c+1] == 'S' and
                        grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'S') or
                        (grid[r-1][c-1] == 'M' and grid[r-1][c+1] == 'M' and
                        grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'S') or
                        (grid[r-1][c-1] == 'S' and grid[r-1][c+1] == 'M' and
                        grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'M') or
                        (grid[r-1][c-1] == 'S' and grid[r-1][c+1] == 'S' and
                        grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'M') 
                    ):
                        count += 1


    return count


def main(grid=None):
    if not grid:
        grid = []
        file_path = os.path.join(os.path.dirname(__file__), 'data/4.txt')
        with open(file_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    grid.append(list(line))
    return count_mas_patterns(grid)

grid_string = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
grid = [list(line) for line in grid_string.strip().split('\n')]
print(main())