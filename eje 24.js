let numP = 29;
let esP = true;
for(let i = 2; i <= numP / 2; i++) {
    if (numP % i === 0) {
        esP = false;
        break;
    }
}
if (esP) {
    console.log("Es primo");
} else {
    console.log("No es primo");
}