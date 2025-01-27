def Quick_Sort(arr):
    # Base case: If the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element (using the last element as the pivot)
    pivot = arr[-1]
    
    # Partitioning step: Create two lists, one for elements less than pivot and one for elements greater than pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively apply Quick Sort on left and right sub-arrays and combine them with the pivot
    return Quick_Sort(left) + [pivot] + Quick_Sort(right)

# Input and usage
no = int(input('Enter how many numbers to sort: '))
list1 = [int(input()) for i in range(no)]

sorted_list = Quick_Sort(list1)
print('Sorted List:', sorted_list)
