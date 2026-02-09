def merge(numbers, left_first, left_last, right_last):
    merged_size = right_last - left_first + 1
    merged_nums = [0] * merged_size
    merge_pos = 0
    left_pos = left_first
    right_pos = left_last + 1

    while left_pos <= left_last and right_pos <= right_last:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_nums[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_nums[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1

    while left_pos <= left_last:
        merged_nums[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1

    while right_pos <= right_last:
        merged_nums[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1

    for i in range(merged_size):
        numbers[left_first + i] = merged_nums[i]