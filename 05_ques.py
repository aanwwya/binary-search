# 5. given array 
arr = [6, 10, 14, 19, 25, 32, 38, 44, 51, 60, 71]
target = 25

# write a binary search function that returns the index of 25, 
# or -1 if it isn't found

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