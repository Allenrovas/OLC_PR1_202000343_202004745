
console.log("=======================================================================");
console.log("==================================IF===================================");
console.log("=======================================================================");

let comp : number= 56;
if (comp > 50){
    console.log("IF CORRECTO");
} else if (comp === 56) {
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
} else if (aux === comp){
    console.log("PRIMER IF INCORRECTO");
    if (true && (aux === 1)){
        console.log("SEGUNDO IF INCORRECTO");
    } else if (aux > 10){
        console.log("SEGUNDO IF INCORRECTO");
    } else {
        console.log("SEGUNDO IF CORRECTO");
    };
};