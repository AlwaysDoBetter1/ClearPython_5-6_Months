'''
binary search of list
'''


# list should be sorted for working binary search
def binary_search(list: list, item: (str, int)) -> int:  # annotations of types
    low = 0  # min boundary
    high = len(list) - 1  # max boundary

    while low <= high:
        mid = (low + high) // 2  # average for binary search
        guess = list[mid]
        if guess == item:  # if element was found
            return mid  # return index and break while
        if guess > item:
            # if the average is bigger than the desired value, cut off the right half of the list and find new average
            high = mid - 1
        else:
            # if the average is lesser than the desired value, cut off the left half of the list and find new average
            low = mid + 1
    return None  # if element not found


mlist = [2, 4, 5, 6, 8, 10]
print(binary_search(mlist, 4))  # return index of element: 1
