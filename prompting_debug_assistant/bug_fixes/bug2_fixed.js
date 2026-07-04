function isEven(number) {
    return number % 2 === 0;
}

const numbers = [2, 5, 8, 11];

for (const number of numbers) {
    if (isEven(number)) {
        console.log(`${number} is even`);
    }
}