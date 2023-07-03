let array = [32, 21, 7, 89, 56, 909, 109, 2];


console.log("=======================================================================");
console.log("==================================IF===================================");
console.log("=======================================================================");

if (array[4] > 50){
    console.log("IF CORRECTO");
} else if (array[4] === 56) {
    console.log("IF INCORRECTO");
} else {
    console.log("IF INCORRECTO");
};

console.log("");
console.log("=======================================================================");
console.log("=============================IFs ANIDADOS==============================");
console.log("=======================================================================");
let aux:number = 10;
if (aux > 0){
    console.log("PRIMER IF CORRECTO");
    if (true && (aux === 1)){
        console.log("SEGUNDO PR IF INCORRECTO");
    } else if (aux > 10){
        console.log("SEGUNDO SE IF INCORRECTO");
    } else{
        console.log("SEGUNDO IF CORRECTO");
    };
} else if (aux <= 3){
    console.log("PRIMER IF INCORRECTO");
    if (true && (aux === 1)){
        console.log("SEGUNDO IF INCORRECTO");
    } else if (aux > 10){
        console.log("SEGUNDO IF INCORRECTO");
    } else {
        console.log("SEGUNDO IF CORRECTO");
    };
} else if (aux === array[4]){
    console.log("PRIMER IF INCORRECTO");
    if (true && (aux === 1)){
        console.log("SEGUNDO IF INCORRECTO");
    } else if (aux > 10){
        console.log("SEGUNDO IF INCORRECTO");
    } else {
        console.log("SEGUNDO IF CORRECTO");
    };
};

console.log("");
console.log("=======================================================================");
console.log("=================================WHILE=================================");
console.log("=======================================================================");

let index: number;
index = 0;
while (index >= 0){
    if (index === 0){ 
        index = index + 100;
    }else if (index > 50){ 
        index = index / 2 - 25;
    }else{ 
        index = (index / 2) - 1;
    };

    console.log(index);
};

console.log("");
console.log("=======================================================================");
console.log("================================WHILE-2================================");
console.log("=======================================================================");

index= -2;
index = index + 1;

console.log(index);

while (index !== 12) {
    index = index + 1;
    
    if (index === 0 || index === 1 || index === 11 || index === 12) {
        console.log("*********************************************************************************************************");
    }else if (index === 2) {
        console.log("**********  ***************  ******                 ******                 ******              **********");
    }else if (index >= 3 && index <= 5) {
        console.log("**********  ***************  ******  *********************  *************  ******  **********************");
    }else if (index === 6) {
        console.log("**********  ***************  ******                 ******                 ******  **********************");
    } else if (index >= 7 && index <= 9) {
        console.log("**********  ***************  ********************   ******  *************  ******  **********************");
    } else if (index === 10) {
        console.log("**********                   ******                 ******  *************  ******              **********");
    };
};

console.log("");

let a:number = -1;
while (a < 5){
    a = a + 1;
    if (a === 3){
        console.log("a");
        continue;
    } else if (a === 4){
        console.log("b");
        break;
    };
    console.log("El valor de a es: ", a, ", ");
};

console.log("");
console.log("Se debió imprimir");
console.log("");
console.log("");
console.log("=======================================================================");
console.log("==================================FOR==================================");
console.log("=======================================================================");

for (let i=0; i<=9; i++){
    let output = "";
    for (let j =0; j<10; j++){
        output = output + " ";
    };

    for (let k =0; k<10; k++ ){
        output = output + "* ";
    };


    console.log(output);

};


console.log("");
console.log("=======================================================================");
console.log("=================================FOR-2=================================");
console.log("=======================================================================");

let arr = [1,2,3,4,5,6];
for (let al of [1,2,3,4,5,6]){
    console.log(arr[al] === 1, arr[al] === 2, arr[al] === 3, arr[al] === 4, arr[al] === 5, arr[al] === 6);
};

console.log("");
console.log("=======================================================================");
console.log("=================================FOR-3=================================");
console.log("=======================================================================");
for (let e of [1,2,3,4,5,6]){
    if(6 > e){
        console.log(e+arr[e],e+arr[e],e+arr[e],e+arr[e],e+arr[e],e+arr[e]);
    };
};

console.log("");
console.log("=======================================================================");
console.log("=================================FOR-4=================================");
console.log("=======================================================================");
for (let letra of "Calificacion de Intermedio"){
    console.log(letra);
};