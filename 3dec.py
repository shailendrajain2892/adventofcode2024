import os
import re

def mul(n1, n2):
    return n1*n2

def ignore_char_mul_num(string:str):
    total_sum=0
    # pattern1  = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    # matches = re.findall(pattern1, string)
    # print(matches)
    enabled=True
    for match in re.finditer(pattern, string):
        if match.group() == "don't()":
            enabled = False
        elif match.group() == 'do()':
            enabled = True
        elif match.group().startswith('mul'):
            if enabled:
                total_sum += eval(match.group())
    return total_sum


def main():
    # Reading the uploaded file into two lists: one for the first column and one for the second column.
    file_path = os.path.join(os.path.dirname(__file__), 'data/3.txt')
    total_sum=0
    all_lines=""
    # Read the file and populate the string
    with open(file_path, 'r') as file:
        for line in file:
            all_lines+=line
    return ignore_char_mul_num(all_lines)

# mixed_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# print(ignore_char_mul_num(mixed_str))
mixed_str_with_do_dont = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# print(ignore_char_mul_num_with_do_dont(mixed_str_with_do_dont))
print(ignore_char_mul_num(mixed_str_with_do_dont))
print(main())
