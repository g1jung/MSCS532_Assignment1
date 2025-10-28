def insertionSort(arr):
    length = len(arr);

    if length < 2:
        return  #no need to sort less than 2
    
    for i in range(1, length):
        currNum = arr[i]
        