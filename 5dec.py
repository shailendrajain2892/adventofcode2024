from collections import defaultdict, deque
import os

def is_update_ordered(update, rules):
    page_position = {page:i for i, page in enumerate(update)}
    for x, y in rules:
        if x in page_position and y in page_position and page_position[x] > page_position[y]:
            return False
    return True

def reorder_update(update, rules):
    """
    Reorder an update based on the ordering rules using topological sort.

    Args:
        update (list): A list of page numbers in the update.
        rules (list): A list of tuples representing ordering rules.

    Returns:
        list: The correctly ordered update.
    """
    # Build a graph for the current update
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    pages_in_update = set(update)
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in pages_in_update if in_degree[node] == 0])
    ordered = []

    while queue:
        node = queue.popleft()
        ordered.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered

def parse_input(input_data):
    sections = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
    updates = [ list(map(int, line.split(',')))for line in sections[1].splitlines()]
    return rules, updates

def sum_middle_pages(input_data):
    rules, updates = parse_input(input_data)
    middle_page_sum=0
    for update in updates:
        if not is_update_ordered(update, rules):
            reordered  = reorder_update(update, rules)
            middle_page = reordered[len(reordered)//2]
            middle_page_sum+=middle_page
    return middle_page_sum

# Example Input
input_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
file_path = os.path.join(os.path.dirname(__file__), 'data/5.txt')
with open(file_path) as f:
    input_data = f.read()
print(sum_middle_pages(input_data))