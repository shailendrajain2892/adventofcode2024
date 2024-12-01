from collections import defaultdict
from typing import Counter


def total_distance(list1, list2):
    total_distance=0
    list1.sort()
    list2.sort()
    for n1, n2 in zip(list1, list2):
        total_distance+=abs(n1-n2)
    return total_distance

def similarity_score(list1, list2 ):
    list2_counter = defaultdict(int)
    for n2 in list2:
        list2_counter[n2]+=1
    return sum(n1*list2_counter[n1] for n1 in list1)

def main():
    # Reading the uploaded file into two lists: one for the first column and one for the second column.
    file_path = 'data/1.txt'

    # Initialize two lists to hold the columns
    list_1 = []
    list_2 = []

    # Read the file and populate the lists
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                col1, col2 = map(int, line.split())
                list_1.append(col1)
                list_2.append(col2)
    
    print(f"similarity score is : {similarity_score(list_1, list_2)}")
    print(f"total distance is : {total_distance(list_1, list_2)}")

main()