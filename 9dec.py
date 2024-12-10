import os


def find_checksum(input_string):
    # input_string =    2333133121414131402
    # create disk map from input string in this format 00...111...2...333.44.5555.6666.777.888899
    disk_map = create_disk_map(input_string)
    print(len(disk_map))
    # print(disk_map)
    # print(disk_map == "00...111...2...333.44.5555.6666.777.888899")
    updated_disk_map = fill_empty_space_with_num(disk_map)
    print(len(updated_disk_map))
    # print(updated_disk_map=="022111222......")
    checksum = calculate_checksum(updated_disk_map)
    return checksum


def create_disk_map(diskmap):
    blocks = []
    is_file = True
    id = 0
    for x in diskmap:
        x = int(x)
        if is_file:
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += "." * x
            is_file = True
    return blocks


def fill_empty_space_with_num(disk_map):
    updated_disk_map = disk_map.copy()
    start = 0
    end = len(disk_map) -1
    while start <= end:
        if disk_map[start] == ".":
            while end > start and disk_map[end] == ".":
                end -= 1
            if end > start:
                updated_disk_map[start] = disk_map[end]
                updated_disk_map[end] = "."
                end -= 1
        start += 1
    # empty_space = len(disk_map) - len(updated_disk_map)
    # updated_disk_map += "." * empty_space
    print(countidandspaces(updated_disk_map))
    print(countidandspaces(disk_map))
    return updated_disk_map

def countidandspaces(input_string):
    count, space = 0, 0
    for char in input_string:
        if char != ".":
            count += 1
        else:
            space += 1
    return count, space


def calculate_checksum(updated_disk_map):
    checksum = 0
    for i, char in enumerate(updated_disk_map):
        if char != ".":
            checksum += (i * int(char))
    return checksum


file_path = os.path.join(os.path.dirname(__file__), 'data/9.txt')
with open(file_path) as f:
    input_string = f.read().strip()
# input_string = "2333133121414131402"
# input_string="12345"
print(len(input_string))
print(find_checksum(input_string))
