let dec = 25;
let bin = "";
while(dec > 0) {
    bin = (dec % 2) + bin;
    dec = Math.floor(dec / 2);
}
console.log(bin)