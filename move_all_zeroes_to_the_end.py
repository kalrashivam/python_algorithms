# Function to move all the zeroes to the end of the array recieved.
def pushZerosToEnd(arr, n):
    # To count all the non zero elements
    count = 0

    for i in range(n):
        if arr[i]!= 0:
            arr[count] = arr[i]
            count += 1

    while count<n:
        arr[count] = 0
        count += 1

# Input array must hold numbers and not strings.
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
# Sends the array and the size as arguments
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:") 
print(arr)