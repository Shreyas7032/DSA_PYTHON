def Merge_Sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]

        # Recursively sort both halves
        Merge_Sort(left_list)
        Merge_Sort(right_list)

        i = 0
        j = 0
        k = 0

        # Merging the two sorted halves
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
                k+=1
            else:
                list[k] = right_list[j]
                j += 1
                k += 1
        
        # If there are any remaining elements in left_list
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
        
        # If there are any remaining elements in right_list
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

# Input and usage
no = int(input('Enter How Many No to sort: '))
list1 = [int(input()) for i in range(no)]
Merge_Sort(list1)
print('Sorted List:', list1)
