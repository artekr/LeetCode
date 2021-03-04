def mergesort(arr: [int]):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sort left half and right half
        mergesort(left_half)
        mergesort(right_half)

        # Start merging
        i, j, k = 0, 0, 0

        while i < len(left_half) or j < len(right_half):
            # Copy the remaining elements of right_half, if there are any
            if i >= len(left_half):
                arr[k] = right_half[j]
                j += 1
            # Copy the remaining elements of left_half, if there are any
            elif j >= len(right_half):
                arr[k] = left_half[i]
                i += 1
            # Compare two sorted array and put it to result array
            else:
                if left_half[i] <= right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            k += 1
        return arr


##########################################
# Mergesort with separate merge function #
##########################################
def mergesort_helper(arr: [int]):
    low = 0
    high = len(arr) - 1
    sorted_arr = sort(arr, low, high)
    return sorted_arr


def sort(arr: [int], low: int, high: int):
    if low < high:
        mid = (low + high - 1) // 2
        sort(arr, low, mid)
        sort(arr, mid + 1, high)
        return merge(arr, low, mid, high)


def merge(arr: [int], low: int, mid: int, high: int):
    left_len = mid - low + 1
    right_len = high - mid

    # create temp arrays 
    left_half = [0] * left_len
    right_half = [0] * right_len

    # Copy data to temp arrays left_half[] and right_half[] 
    for i in range(0, left_len):
        left_half[i] = arr[low + i]

    for j in range(0, right_len):
        right_half[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = low
    while i < len(left_half) or j < len(right_half):
        if i >= len(left_half):
            arr[k] = right_half[j]
            j += 1
        elif j >= len(right_half):
            arr[k] = left_half[i]
            i += 1
        else:
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
        k += 1
    return arr


k = [8, 4, 7, 2, 9, 10, 5, 6, 4, 1]

print(mergesort(k))
print(mergesort_helper(k))

# Expected: [1, 2, 4, 4, 5, 6, 7, 8, 9, 10]
