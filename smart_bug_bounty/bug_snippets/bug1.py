def calculate_average(numbers):
    """Return the average of a list of numbers."""
    if not numbers:
        return 0

    total = 0
    for number in numbers:
        total += number

    return total / (len(numbers) - 1)


def main():
    values = [10, 20, 30]
    print(calculate_average(values))


if __name__ == "__main__":
    main()