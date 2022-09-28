def fetch_input(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()

    numbers = [number.strip() for number in numbers]
    return numbers, len(numbers[0])


def get_most_popular(column, numbers):
    ones = 0
    for number in numbers:
        if number[column] == '1':
            ones += 1

    if ones >= (len(numbers) - ones):
        return '1'

    return '0'


def get_least_popular(column, numbers):
    ones = 0
    for number in numbers:
        if number[column] == '1':
            ones += 1

    if (len(numbers) - ones) > (len(numbers) / 2):
        return '1'

    return '0'


def main():
    numbers, columns = fetch_input('input_files/3.txt')

    oxygen_numbers = numbers.copy()
    co2_numbers = numbers.copy()

    for i in range(columns):
        print(f"Iteration {i}: {oxygen_numbers}")
        most_popular_in_column = get_most_popular(i, oxygen_numbers)
        print(f"Most popular in column {i}: {most_popular_in_column}")
        oxygen_numbers = list(filter(lambda number: number[i] == most_popular_in_column, oxygen_numbers))

    oxygen_generator_rating = int(oxygen_numbers[0], 2)
    print(oxygen_generator_rating)

    for i in range(columns):
        print(f"Iteration {i}: {co2_numbers}")
        if len(co2_numbers) > 1:
            least_popular_in_column = get_least_popular(i, co2_numbers)
            print(f"Least popular in column {i}: {least_popular_in_column}")
            co2_numbers = list(filter(lambda number: number[i] == least_popular_in_column, co2_numbers))

    co2_scrubber_rating = int(co2_numbers[0], 2)
    print(co2_scrubber_rating)

    print(co2_scrubber_rating * oxygen_generator_rating)


if __name__ == "__main__":
    main()
