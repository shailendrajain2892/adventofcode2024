def chceckForIncreasingOrder(report):
    for i, val in enumerate(report):
        if i > 0 and (val - report[i - 1] == 0 or val - report[i - 1] > 3 or val - report[i - 1] < 0):
            return 0
    return 1


def checkForDecreasingOrder(report):
    for i, val in enumerate(report):
        if i > 0 and (report[i - 1] - val == 0 or report[i - 1] - val > 3 or val - report[i - 1] > 0):
            return 0
    return 1


def reports_safe(report):
    # return 1 if report is safe otherwise 0
    if report[1] > report[0]:
        resp = chceckForIncreasingOrder(report)
    else:
        resp = checkForDecreasingOrder(report)
    return resp


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
    file_path = os.path.join(os.path.dirname(__file__), '2.txt')

    # Initialize two lists to hold the columns
    reports_safe_count = 0

    # Read the file and populate the lists
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                report = list(map(int, line.split()))
                reports_safe_count += reports_safe(report)

    return reports_safe_count

print(main())
