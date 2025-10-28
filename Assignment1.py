def insertionSort(arr):
    length = len(arr)

    if length < 2:
        return  #no need to sort less than 2
    
    for i in range(1, length):
        currNum = arr[i]

        loopNum = i-1
        while loopNum >= 0 and currNum < arr[loopNum]:
            arr[loopNum+1] = arr[loopNum]
            loopNum -= 1
        
        arr[loopNum+1] = currNum


arr = [12, 39, 22, 67, 2, 15]
insertionSort(arr)
print(arr)