import math

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(1)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
