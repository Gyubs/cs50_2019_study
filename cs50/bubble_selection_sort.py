def bubble_sort(array):
    for i in range(len(array)):
        swap = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]: 
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
                print(array)
        if swap == False:
            break
                    
    return array

# array = [6, 3, 8, 5, 2, 7, 4, 1]
array = [1, 2, 3, 4, 5, 6, 7, 8]
print(bubble_sort(array))

def selection_sort(array):
    for i in range(len(array)-1):
        min_num = i
        for j in range(i + 1, len(array)):
            if array[min_num] > array[j]:
                min_num = j 
        array[i], array[min_num] = array[min_num], array[i]
        print(array)
    
    return array
        
# print(selection_sort(array))