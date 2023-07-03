function ackerman(m: number, n: number): number {
    if (m === 0) {
        return n + 1;
    } else if (m > 0 && n === 0) {
        return ackerman(m - 1, 1);
    } else {
        return ackerman(m - 1, ackerman(m, n - 1));
    }
}

function hanoi(discos: number, origen: number, auxiliar: number, destino: number){
    if (discos === 1) {
    console.log("Mover de ", origen, " a ", destino);
    } else {
    hanoi(discos - 1, origen, destino, auxiliar);
    console.log("Mover de ", origen, " a ", destino);
    hanoi(discos - 1, auxiliar, origen, destino);
    }
}

function factorial(num: number): number {
    if (num === 1) {
        return 1;
    } else {
        return num * factorial(num - 1);
    }
}
console.log(factorial(5));
console.log(ackerman(3, 5));
hanoi(3, 1, 2, 3);