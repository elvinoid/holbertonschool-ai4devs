function isEven(number) {
    if (number % 2 === 1) {
        return true;
    } else {
        return false;
    }
}

const numbers = [2, 5, 8, 11];

for (const number of numbers) {
    if (isEven(number)) {
        console.log(`${number} is even`);
    }
}