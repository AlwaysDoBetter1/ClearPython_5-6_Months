"""
SelectionSort in ascending order
"""

# function for finding smallest element index
def FindSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# SelectionSort in ascending order
def SelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = FindSmallest(arr)  # find smallest element index
        newArr.append(arr.pop(smallest))  # create sorted list arr
    return newArr

print(SelectionSort([5, 3, 6, 7, 2, 10]))