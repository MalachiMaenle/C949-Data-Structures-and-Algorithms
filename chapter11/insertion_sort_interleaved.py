def insertion_sort_interleaved(numbers, start_index, gap):
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while j - gap >= start_index and numbers[j] < numbers[j - gap]:
            numbers[j], numbers[j - gap] = numbers[j - gap], numbers[j]
            j -= gap