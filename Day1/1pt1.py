

def fetch_input(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()

    numbers = [int(number.strip()) for number in numbers]
    return numbers


def main():
    numbers = fetch_input('input_files/1.txt')
    highest = numbers[0]
    increases = 0
    for number in numbers:
        if number > highest:
            increases += 1
        highest = number

    print(increases)


if __name__ == "__main__":
    main()
