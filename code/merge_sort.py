"""
Merge Sort
This is yet another very common sorting algorithm.
Here the philosophy is to divide and conquer.
Basically you divide the list in to minimum size lists, (which length is 1;))
and then merge it back while sorting it on the way.

The time/space complexity of it is O(nlog n).
"""

def divide(input_list):
    middle_point = len(input_list) // 2
    return input_list[:middle_point], input_list[middle_point:]

def merge(left, right):
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    left_half, right_half = divide(input_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
