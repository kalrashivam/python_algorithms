def binary_search_modified(arr, start, end):
    if start > end:
        return end + 1

    if start != arr[start]:
        return start

    mid = int((start + end) / 2)

    if arr[mid] == mid:
        return binary_search_modified(arr, mid+1, end)

    return binary_search_modified(arr, start, mid)


# Input sorted array must hold numbers and not strings.
arr = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
n = len(arr)

# Sends the array and the size as arguments
missing_element = binary_search_modified(arr, 0, n-1)
print("And the missing element is: %d", missing_element)

