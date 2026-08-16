# 6. binary search - first occurrence 
# a sorted array can contain the same number multiple times

arr = [2, 4, 4, 4, 7, 9, 12]
target = 4

def first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            answer = mid
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return answer


result = first_occurrence(arr, target)
print(result)