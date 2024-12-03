def is_safe(report):
    # return true if safe otherwise false
    decreasing = all([1<= report[i] - report[i+1] <= 3 for i in range(len(report)-1)])
    increasing = all([1<= report[i+1] - report[i] <= 3 for i in range(len(report)-1)])
    return increasing or decreasing

def can_be_safe_with_dampner(report):
    for i in range(len(report)):
        modified_report = report[:i]+report[i+1:]
        if is_safe(modified_report):
            return True
    return False

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# data = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """
#
# # Split the data into lines and then split each line into numbers
# list_of_lists = [list(map(int, line.split())) for line in data.strip().split('\n')]
#
# for list in list_of_lists:
#     print(reports_safe(list))

import os


def main():
    # Reading the uploaded file into two lists: one for the first column and one for the second column.
    file_path = os.path.join(os.path.dirname(__file__), 'data/2.txt')

    # Initialize two lists to hold the columns
    reports_safe_count = 0

    # Read the file and populate the lists
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                report = list(map(int, line.split()))
                if is_safe(report) or can_be_safe_with_dampner(report):
                    reports_safe_count += 1

    return reports_safe_count

print(main())
