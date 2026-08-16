# 2. sorted array 
arr = [3, 7, 11, 15, 19, 24, 31, 42, 50]
target = 31

# write a binary search function that returns the index of 31, 
# or -1 if it isn't found.

def binary_search(arr, target):
    low = 0 
    high = len(arr)-1
    
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
