console.log("=======================================================================");
console.log("==========================FUNCIONES Y RETURN===========================");
console.log("=======================================================================");

function potenciaNativa(base: number, exponente: number): number {
    let resultado: number = base;
    while (exponente > 1) {
        resultado = resultado * base;
        exponente = exponente - 1;
    }
    return resultado;
}

console.log(potenciaNativa(5, 7));
console.log(potenciaNativa(2, 2));
console.log(potenciaNativa(4, 2));

function sumarTodo(num1: number, num2: number): number {
    let result: number = 0;
    if (num1 < 0 || num2 < 0) {
        return -1;
    }

    while (num1 > 0 || num2 > 0) {
        result = result + (num1 + num2);
        num1 = num1 - 1;
        num2 = num2 - 1;
    }
    return result;
}

console.log(sumarTodo(5, 4));
console.log(sumarTodo(-1, -5));
console.log(sumarTodo(7, 7));
