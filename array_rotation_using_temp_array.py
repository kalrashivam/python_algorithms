# Function to left rotate an array using an temporary array.
def leftRotate(arr, d, n):
    # Temp array to save d elements
    temp = list()

    # moving d elements to a temporary array
    for i in range(d):
       temp.append(arr[i])

    # rotating the array
    for z in range(d):
        j = 0
        while j < n - 1:
            arr[j] = arr[j+1]
            j += 1

    # adding the elements in the temp array to the end of the main array
    i = 0
    while i < d:
        arr[(n-d)+i] = temp[i]
        i += 1

# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")

# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)