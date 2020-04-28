# To rearrange a sorted array in the max min form.
# for e.g. given_array = [1,2,3,4,5,6,7,8,9]
# answer_array = [9,1,8,2,7,3,6,4,5]

def Convert_to_max_min(arr, n):
    temp_arr = []

    # to denote the begining of the array
    start = 0

    # to denote the end of the array
    end = n-1

    max = True
    while start <= end:
        if max:
            temp_arr.append(arr[end])
            end -=1
            max = False
        else:
            temp_arr.append(arr[start])
            start +=1
            max = True

    return temp_arr

# Code to run the program
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print("Given Array")
print(arr)
print("Answer Array")
print(Convert_to_max_min(arr, n))