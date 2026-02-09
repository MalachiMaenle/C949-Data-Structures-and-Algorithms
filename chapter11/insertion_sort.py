def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp

            j -= 1