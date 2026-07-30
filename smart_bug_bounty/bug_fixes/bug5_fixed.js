function calculateTotal(items, discountPercent) {
    if (!Array.isArray(items)) {
        return 0;
    }

    let total = 0;

    for (const item of items) {
        total += item.price * item.quantity;
    }

    if (discountPercent > 0) {
        total = total - (total * discountPercent / 100);
    }

    return total;
}

function main() {
    const items = [
        { price: 10, quantity: 2 },
        { price: 5, quantity: 4 }
    ];

    console.log(calculateTotal(items, 10));
}

main();