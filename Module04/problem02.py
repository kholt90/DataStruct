
def SelectionSort(inputList):
    # Traverse through all array elements 
    for i in range(len(inputList)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(inputList)):
            if inputList[min_idx] > inputList[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        inputList[i], inputList[min_idx] = inputList[min_idx], inputList[i]
