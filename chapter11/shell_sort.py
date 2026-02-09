from chapter11.insertion_sort_interleaved import insertion_sort_interleaved

def shell_sort(numbers, gap_values):
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)