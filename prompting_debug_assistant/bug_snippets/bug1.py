def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    if len(numbers) == 0
        return 0

    return total / len(numbers)


values = [10, 20, 30]
print(calculate_average(values))