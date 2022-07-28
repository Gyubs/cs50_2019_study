def linear_search(value, array):
    for i in array:
        if i == value:
            return True
    return False


def binary_search(value, array):
    first, last = 0, len(array)
    
    while first < last:
        mid = (first+last) // 2
        if value == array[mid]:
            return True
        elif value < array[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False

value = 10
array = [1,2,3,4,5,6,7,8,9,10]

print(linear_search(value, array))
print(binary_search(value, array))