# Function to reverse the array
def reverseList(A, start_element, last_element):
    while start_element < last_element:
        A[start_element], A[last_element] = A[ast_element], A[start_element]
        start_element += 1
        last_element -= 1

# Running program
A = [1, 2, 3, 4, 5, 6] 
print(A)
reverseList(A, 0, 5)
print("List after reversing:- ")
print(A)