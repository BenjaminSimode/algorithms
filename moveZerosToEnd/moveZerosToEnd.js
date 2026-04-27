function moveZerosToEnd(arr) {
    const arrLength = arr.length;

    if (arrLength < 2) {
        return arr;
    }

    let counter = 0;
    
    for (const val of arr) {
        if (val !== 0) {
            arr[counter] = val;
            counter += 1;
        }
    }

    for (let i = counter; i < arrLength; i++) {
        arr[i] = 0;
    }

    return arr;
}

console.log(moveZerosToEnd([0, 1, 0, 3, 12]));
