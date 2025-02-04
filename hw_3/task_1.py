
import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1

setup_code = "from __main__ import insertion_sort, merge_sort, random"
test_code_insertion = '''
arr = [random.randint(0, 100000) for _ in range(10000)]
insertion_sort(arr)
'''
test_code_merge = '''
arr = [random.randint(0, 100000) for _ in range(10000)]
merge_sort(arr)
'''
test_code_timsort = '''
arr = [random.randint(0, 100000) for _ in range(10000)]
arr.sort()
'''

time_insertion = timeit.timeit(stmt=test_code_insertion, setup=setup_code, number=10)
time_merge = timeit.timeit(stmt=test_code_merge, setup=setup_code, number=10)
time_timsort = timeit.timeit(stmt=test_code_timsort, setup=setup_code, number=10)

print("Insertion Sort:", time_insertion)
print("Merge Sort:", time_merge)
print("Timsort (built-in sort):", time_timsort)
