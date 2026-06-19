let n1 = 10;
let n2 = 2;
let op = "/";
switch(op) {
    case "+":
        console.log(n1 + n2);
        break
    case "-":
        console.log(n1 - n2);
        break
    case "*":
        console.log(n1 * n2);
        break
    case "/":
        if (n2 !== 0) {
            console.log(n1 / n2);
        } else {
            console.log("Error")
        }
        break
}