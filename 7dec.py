from itertools import product

def check_equation_validity(nums, ops):
    result = nums[0]
    for i in range(len(nums)-1):
        if ops[i] == "+":
            result+=nums[i+1]
        else:
            result*=nums[i+1]
    return result

def is_equation_valid(test_value, nums):
    nums_position = len(nums)-1
    for ops in product("+*", repeat=nums_position):
        if check_equation_validity(nums, ops) == test_value:
            return True
    return False

def calculate_total_calibration(input_data):
    total = 0
    for line in input_data.strip().split("\n"):
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        nums = list(map(int, numbers.split(" ")))
        if is_equation_valid(test_value, nums):
            total+=test_value
    return total

# Example Input
input_data = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

# Calculate the total calibration result
print(calculate_total_calibration(input_data))  # Output should match the example

file_path = "data/7.txt"
with open(file_path) as f:
    input_data = f.read()
    print(calculate_total_calibration(input_data)) 