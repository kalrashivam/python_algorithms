def leftRotate(arr, d, n):
    temp = list()

    for i in range(d):
       temp.append(arr[i])

    for z in range(d):
        print(z)
        j = 0
        while j < n:
            print(j)
            j += 1
            arr[j] = arr[j+1]

    printArray(arr, 7)
    # i = 0
    # while d>0:
    #     arr[(n-d) + i - 1] = temp[i]
    #     i += 1
    #     d -= 1

# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")

# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
# printArray(arr, 7)