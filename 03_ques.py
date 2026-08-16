# 3. target doesn't exist 

arr = [4, 9, 13, 18, 27, 35, 41, 56, 63]
target = 10

# no 10 in arr

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