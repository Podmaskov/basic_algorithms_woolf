def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            # Found the target
            return (count, arr[mid])  # Second element is x itself
    # Not found, smallest element >= x is at position low (if valid)
    if low < len(arr):
        return (count, arr[low])
    else:
        return (count, None)

arr = [1.3, 3.4, 4.5, 10.1, 40.5]
x = 3.3
result = binary_search(arr, x)
if result != -1:
    print(result)
else:
    print("Element is not present in array")