def quick_sort(arr):
    if len(arr) <= 1:
        return arr  

    pivot = arr[0]  
    less = [x for x in arr[1:] if x <= pivot]  
    greater = [x for x in arr[1:] if x > pivot]  

    return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [2,56,36,45,89,7,5]

arr2 = quick_sort(arr)
print(arr2)