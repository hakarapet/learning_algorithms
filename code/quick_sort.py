"""
Quick sort algorithm is know for its simplicity
and also for it efficiency.
It has time/space complexity of O(nlog n).
If you don't know what is this O(n) means, read Big O notation
"""

def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    pivot = input_list.pop()
    higher = []
    lower = []

    for i in input_list:
        if i > pivot:
            higher.append(i)
        else:
            lower.append(i)

    return quick_sort(lower) + [pivot] + quick_sort(higher)