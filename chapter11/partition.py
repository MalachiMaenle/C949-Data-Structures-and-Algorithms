def partition(numbers, low_index, high_index):
    midpoint = low_index + (high_index - low_index) // 2
    pivot = numbers[midpoint]

    done = False
    while not done:
        while numbers[low_index] < pivot:
            low_index += 1

        while pivot < numbers[high_index]:
            high_index -= 1

        if low_index >= high_index:
            done = True
        else:
            numbers[low_index], numbers[high_index] = numbers[high_index], numbers[low_index]

            low_index += 1
            high_index -= 1

    return high_index