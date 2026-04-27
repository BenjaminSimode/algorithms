from typing import List

def moveZerosToEnd(arr: List[int]) -> List[int]:
    array_length = len(arr)

    if array_length < 2:
        return arr

    counter = 0

    for val in arr:
        if val != 0:
            arr[counter] = val
            counter += 1
    
    while counter < array_length:
        arr[counter] = 0
        counter += 1

    return arr

print(moveZerosToEnd([0, 1, 0, 3, 12]))
