def calculate_average(numbers):
    """Calculate the average of numbers."""
    if not numbers:
        return 0

    total = 0
    for number in numbers:
        total += number

    return total / (len(numbers) - 1)


def main():
    values = [10, 20, 30, 40]
    average = calculate_average(values)
    print("Average:", average)


if __name__ == "__main__":
    main()