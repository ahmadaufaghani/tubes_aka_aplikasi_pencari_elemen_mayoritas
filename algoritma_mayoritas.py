def findModeLoop(arr, n):
    max_count = 0
    mode = arr[0]
    
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > max_count:
            max_count = count
            mode = arr[i]
    
    return mode

def findModeRecursive(arr, n, index=0, check_index=0, mode=0, max_count=0, current_count=0):
    if index == n:
        return mode
    elif check_index < n:
        if arr[check_index] == arr[index]:
            current_count += 1
        return findModeRecursive(arr, n, index, check_index + 1, mode, max_count, current_count)
    else:
        if current_count > max_count:
            mode = arr[index]
            max_count = current_count
        return findModeRecursive(arr, n, index + 1, 0, mode, max_count, 0)
