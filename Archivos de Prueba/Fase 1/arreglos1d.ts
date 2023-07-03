function swap(a : number , b : number , arreglo : any[]) {
    
    let temp = arreglo[a];
    
    arreglo[a] = arreglo[b];
    arreglo[b] = temp;
    
}

function bubbleSort(arreglo : any[]) {
    for (let i = 0; i < 16 - 1; i++) {
        for (let j = 0; j < 16 - 1; j++) {
        if (arreglo[j] > arreglo[j + 1]) {
            swap(j, j + 1, arreglo);

        }
        }
    }
}

function insertionSort(arr: any[]) {
    for (let i = 1; i < arr.length; i++) {
        let j = i;
        let temp = arr[i];
        while (j > 0 && arr[j - 1] > temp) {
        arr[j] = arr[j - 1];
        j = j - 1;
    }
    arr[j] = temp;
    }
}



let arreglo = [32, 7 * 3, 7, 89, 56, 909, 109, 2, 9, 9874 ^ 0, 44, 3, 820 * 10, 11, 8 * 0 + 8, 10];
bubbleSort(arreglo);
console.log("BubbleSort => ", arreglo);