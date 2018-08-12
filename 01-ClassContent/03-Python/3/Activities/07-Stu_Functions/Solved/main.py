# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Write a main function that calls the average function with test data
# and print the results to the console.
def main():
    print(average([1, 5, 9]))
    print(average(range(11)))

