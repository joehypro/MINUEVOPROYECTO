let col = 12;
while(col !== 1) {
    console.log("col");
    if (col % 2 === 0) {
        col = col / 2;
    } else {
        col = col * 3 + 1;
    }
}
console.log("col");