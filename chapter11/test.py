import numpy
import time
from chapter11.linear_search import linear_search
from chapter11.binary_search import binary_search
from chapter11.selection_sort import selection_sort
from chapter11.insertion_sort import insertion_sort
from chapter11.shell_sort import shell_sort
from chapter11.quicksort import quicksort
from chapter11.merge_sort import merge_sort

print('\n\033[1;32m' + '-----Chapter 11-----' + '\033[0m')

numList = numpy.random.randint(0, 10000, size=10000)
print('\033[96m' + f'numList: {numList}' + '\033[0m')

print('\n\033[31m' + 'Linear Search: ' + '\033[0m')
# region Linear Search test
key = numpy.random.randint(0,100)
key_index = linear_search(numList, key)

if key_index == -1:
    print(f"{key} was not found.")
else:
    print(f"Found {key} at index {key_index}.")
# endregion
# region Linear Search notes
# starts from the beginning of a list and checks each element until the search key is found
# endregion

print('\n\033[31m' + 'Binary Search: ' + '\033[0m')
# region Binary Search test
key = numpy.random.randint(0,100)
key_index = binary_search(numList, key)

if key_index == -1:
    print(f"{key} was not found.")
else:
    print(f"Found {key} at index {key_index}.")
# endregion
# region Binary Search notes
# A search algorithm used to search through sorted lists
# checks the middle of the set
# if key is less than middle, check middle of left set
# if key is greater than middle, check middle of right set
# repeat until key is found
# endregion

# region Constant time operations notes
# An operation that always operates in the same amount of time, regardless of input values
# addition, subtraction, multiplication, division of fixed size integer or floating point values
# assignment of a reference or other fixed size data value
# comparison of two fixed size data values
# read or write a list element to a particular index
# endregion

# region Growth of functions and complexity
# upper bound - anything >= worst case runtime
# lower bound - anything <= best case runtime
# O notation - provides a growth rate for an algorithms upper bound - N>=N0,T(N)<=c*f(N)
# Ω notation - provides a growth rate for an algorithms lower bound - N>=N0,T(N)>=c*f(N)
# Θ notation - provides a growth rate that is both an upper and lower bound - both
# endregion

# region O notation notes
# Big O notation - mathematical way of describing how a function (running time of an algorithm) generally behaves in relation to the input size
# all functions that have the same growth rate are characterized by the same Big O notation
# endregion

print('\n\033[31m' + 'Selection Sort: ' + '\033[0m')
# region Selection Sort test
selection_sort_numList = numList

start_time = time.perf_counter()
selection_sort(selection_sort_numList)
end_time = time.perf_counter()

duration = (end_time - start_time) * 1000

print(f"Sort took {duration:.4f} milliseconds.")
# endregion
# region Selection Sort notes
# treats the input as two parts, a sorted part and an unsorted part, and repeatedly selects the minimum value to move from the unsorted part to the end of the sorted part
# endregion

print('\n\033[31m' + 'Insertion Sort: ' + '\033[0m')
# region Insertion Sort test
insertion_sort_numList = numList

start_time = time.perf_counter()
insertion_sort(insertion_sort_numList)
end_time = time.perf_counter()

duration = (end_time - start_time) * 1000

print(f"Sort took {duration:.4f} milliseconds.")
# endregion
# region Insertion Sort notes
# treats the input as a sorted and unsorted part
# inserts the next value from the unsorted part into the correct index of the sorted part
# endregion

print('\n\033[31m' + 'Shell Sort: ' + '\033[0m')
# region Shell Sort test
shell_sort_numList = numList

start_time = time.perf_counter()
shell_sort(shell_sort_numList, [40, 13, 4, 1])
end_time = time.perf_counter()

duration = (end_time - start_time) * 1000

print(f"Sort took {duration:.4f} milliseconds.")
# endregion
# region Shell Sort notes
# treats the input as a collection of interleaved lists
# sorts each list individually with a variant of the insertion sort algorithm
# uses gap values to determine the number of interleaved lists
# gap value - a positive integer representing the distance between elements in an interleaved list
# if an element is at index i, the next element is at index i + gap value
#
# instead of creating new lists for each gap value, an insertion sort for interleaved lists is used
# endregion

print('\n\033[31m' + 'Quicksort: ' + '\033[0m')
# region Quicksort test
quicksort_numList = numList

start_time = time.perf_counter()
quicksort(quicksort_numList, 0, len(quicksort_numList) - 1)
end_time = time.perf_counter()

duration = (end_time - start_time) * 1000

print(f"Sort took {duration:.4f} milliseconds.")
# endregion
# region Quicksort notes
# repeatedly partitions the input into low and high parts (each part unsorted)
# recursively sorts each partition
# pivot - any value within the list being sorted and is commonly the middle elements value
# once the pivot is chosen the quicksort divides the list into two parts, referred to as the low and high partitions
# all values in the low partition are <= to the pivot
# all values in the high partition are >= the pivot
# uses two index variables, a low index and a high index initialized to the left and right sides of the current elements being sorted
# endregion

print('\n\033[31m' + 'Merge Sort: ' + '\033[0m')
# region Merge Sort test
merge_sort_numList = numList

start_time = time.perf_counter()
merge_sort(merge_sort_numList, 0, len(merge_sort_numList) - 1)
end_time = time.perf_counter()

duration = (end_time - start_time) * 1000

print(f"Sort took {duration:.4f} milliseconds.")
# endregion
# region Merge Sort notes
# divides the list into two halves
# recursively sorts each half
# merges the sorted halves to produce a sorted list
# endregion

print('\n\033[31m' + ': ' + '\033[0m')
# region  test
# endregion
# region  notes
# endregion

print('\n\033[31m' + ': ' + '\033[0m')
# region  test
# endregion
# region  notes
# endregion

print('\n\033[31m' + ': ' + '\033[0m')
# region  test
# endregion
# region  notes
# endregiony
























