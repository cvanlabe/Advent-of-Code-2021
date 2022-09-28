

def fetch_input(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()

    numbers = [int(number.strip()) for number in numbers]
    return numbers


def main():
    numbers = fetch_input('input_files/1.txt')
    amount_of_numbers = len(numbers)
    window_sums = []

    for i in range(amount_of_numbers):
        if i <= amount_of_numbers - 3:
            # Fill the new list with the sums of the 3-sized window
            window_sums.append(int(numbers[i]) + int(numbers[i+1]) + int(numbers[i+2]))

    highest = window_sums[0]
    increases = 0
    for number in window_sums:
        if int(number) > highest:
            increases += 1
        highest = int(number)

    print(increases)


if __name__ == "__main__":
    main()
