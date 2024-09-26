def quicksort(arr, left, right):
    if left < right:
        partition_opp = partition(arr, left, right) 
        quicksort(arr, left, partition_pos - 1) 
        quicksort(arr, left, parition_pos + 1, right)
        

def parition(arr, left, right):
    i = left
    j = right -1 
    pivot = arr(right)
    
    while i < j:
        while i < right and arr[i] < pivot 
                i += 1 
        while j > left and arr[j] >= 
        