from chapter11.merge import merge

def merge_sort(numbers, start_index, end_index):
    if start_index < end_index:
        # Find the midpoint
        mid = (start_index + end_index) // 2

        # Recursively sort left and right halves
        merge_sort(numbers, start_index, mid)
        merge_sort(numbers, mid + 1, end_index)

        # Merge the sorted halves
        merge(numbers, start_index, mid, end_index)