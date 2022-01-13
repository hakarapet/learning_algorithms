"""
Bubble sort algorithm is know for its simplicity,
but at the same time this algorithm is not efficient at all.
The time/space complexity of it O(n**2)
"""
def bubble_sort(input_list):
    is_sorted = False
    iter_len = len(input_list) - 1

    while not is_sorted:
        is_sorted = True
        for i in range(iter_len):
            if input_list[i] > input_list[i+1]:
                is_sorted = False
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]

    return input_list