from collections import defaultdict


def find_nodes(grid):
    nodeMap = defaultdict(set)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                nodeMap[grid[row][col]].add((row,col))
    return nodeMap


unique_antinodes = set()
all_line_antinodes = set()


def count_antinodes(grid):
    antennas = find_nodes(grid)
    rows, cols = len(grid), len(grid[0])
    # Iterate over all potential grid locations
    for r in range(rows):
        for c in range(cols):
            # Check each frequency group
            for freq, positions in antennas.items():
                for (r1, c1) in positions:
                    for (r2, c2) in positions:
                        if (r1, c1) != (r2, c2):
                            # Calculate distances
                            d1 = abs(r - r1) + abs(c - c1)
                            d2 = abs(r - r2) + abs(c - c2)

                            # Calculate slopes to ensure alignment
                            dr1, dr2 = r - r1, r - r2
                            dc1, dc2 = c - c1, c - c2

                            # Check if (r, c) aligns with (r1, c1) and (r2, c2)
                            if dr1 * dc2 == dc1 * dr2:
                                if (d1 == 2 * d2 or d1 * 2 == d2) and 0 <= r < rows and 0 <= c < cols:
                                    unique_antinodes.add((r, c))
                                if 0 <= r < rows and 0 <= c < cols:
                                    all_line_antinodes.add((r, c))

    return len(all_line_antinodes)
input_data = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

def parse_input(input_data):
    grid = []
    for line in input_data.strip().split("\n"):
        grid.append(list(line))
    print(grid)
    return grid

with open('data/8.txt') as f:
    input_data = f.read()
grid = parse_input(input_data)
print(count_antinodes(grid))