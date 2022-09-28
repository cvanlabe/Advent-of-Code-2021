def fetch_input(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()

    numbers = [number.strip() for number in numbers]
    return numbers, len(numbers[0])


def main():
    numbers, columns = fetch_input('input_files/3.txt')
    number_of_numbers = len(numbers)

    # Dictionary to track for each column of a binary number the amount of 1's and 0's
    column = {}

    for number in numbers:
        for i in range(columns):
            # If it's a 1, add it to the column.. we don't care about 0
            if i not in column:
                column[i] = int(number[i])
            else:
                column[i] += int(number[i])

    gamma_rate = ""
    epsilon_rate = ""

    for k, v in column.items():
        # if the amount of 1s (v) is more than half of the numbers, most common is 1
        # => gamma_rate add 1, epsilon_rate add 0
        if v > (number_of_numbers / 2):
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(gamma_rate, int(gamma_rate, 2), epsilon_rate, int(epsilon_rate, 2))

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == "__main__":
    main()
