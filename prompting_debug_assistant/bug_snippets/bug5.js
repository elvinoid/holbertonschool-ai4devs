const cart = [19.99, 24.50, "15.25"];

let total = 0;

for (const item of cart) {
    total += item;
}

console.log("Total:", total);