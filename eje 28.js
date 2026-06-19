let perf = 28;
let sPerf = 0;
for (let i = 1; i < perf; i++) {
    if (perf % i === 0) {
        sPerf += i;
    }
}
if (sPerf === perf) {
    console.log("Es perfect");
} else {
    console.log("no es perfect");
}