"""
Binary Search
This algorithm is used on sorted lists/arrays.
So your input list should be already sorted.
The goal is to find the index of the search item or,
in cases if the item does not exist, return None.
This algorithm has time/space complexity of O(log n)
"""

def binary_search(search_item, input_list):
    start_index = 0
    end_index = len(input_list) - 1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        middle_value = input_list[middle_index]

        if search_item == middle_value:
            return middle_index
        elif search_item < middle_value:
            end_index = middle_index
        else:
            start_index = middle_index
