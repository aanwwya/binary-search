#  1. given a sorted array and a target value, 
# use binary search to find and return the target’s index, 
# or return -1 if it doesn’t exist.

arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23 

# low = 0 index -> 2
# high =  len(arr) -1 -> 72

low = 0
high = 9

mid = (0 + 9) // 2
mid = 4

low = mid + 1

low = 5
high = 9

mid = (5 + 9) // 2
mid = 7
arr[mid] > target
high = mid - 1

mid = (low + high) // 2
mid = (5 + 6) // 2

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


arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23

result = binary_search(arr, target)

print(result)



