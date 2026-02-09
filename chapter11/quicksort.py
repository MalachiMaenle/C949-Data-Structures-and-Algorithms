from chapter11.partition import partition

def quicksort(numbers, low_index, high_index):
    if high_index <= low_index:
        return

    low_end_index = partition(numbers, low_index, high_index)
    quicksort(numbers, low_index, low_end_index)
    quicksort(numbers, low_end_index + 1, high_index)