"""
Quick sort
"""

def quicksort(array):
    if len(array) < 2:
        return array  # base case
    else:
        pivot = array[0]  # recursive case
        less = [i for i in array[1:] if i <= pivot]  # array with elements lesser than pivot
        greater = [i for i in array[1:] if i > pivot]  # array with elements greater than pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

