def count(arr):
    total = 0
    if len(arr) == 0:
        return 0
    else:
        arr.pop(0)
        total=1+count(arr)
    return total

def find_max(arr):
    if(len(arr) == 0):
        return 0
    first = arr.pop(0)
    max = find_max(arr)
    if(first > max):
        return first
    else:
        return max
        
