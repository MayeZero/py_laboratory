def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        first = arr.pop(0)
        last = sum(arr)
    return first + last
