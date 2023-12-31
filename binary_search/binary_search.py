def binary_search(start, end, target, array):
    while start<=end:

        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target :
            end =  mid
        
        else:
            start = mid
        
        return None

array = [1, 2, 3, 4, 5]
target = 5

result = binary_search(0, len(array) - 1, target, array)
print(result)