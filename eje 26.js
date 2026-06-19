let f1 = 0;
let f2 = 1;
for(let i = 0; i < 15; i++) {
    console.log(f1);
    let prox = f1 + f2;
    f2 = prox;
}