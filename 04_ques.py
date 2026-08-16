# 4. given 
arr = [5, 8, 12, 17, 21, 29, 34, 41, 50, 63, 77]
target = 41

# write a binary search function that returns the index of 41, 
# or -1 if it isn't found.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


result = binary_search(arr, target)
print(result)