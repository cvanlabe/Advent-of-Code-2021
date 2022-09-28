def fetch_input(input_file):
    with open(input_file, 'r') as f:
        commands = f.readlines()

    commands = [command.strip() for command in commands]
    return commands


def main():
    commands = fetch_input('input_files/2.txt')
    destination = {
        'horizontal': 0,
        'vertical': 0,
        'aim': 0,
    }
    for command in commands:
        direction, increment = command.split(' ')
        increment = int(increment)

        if (direction == 'forward'):
            destination['horizontal'] += increment
            destination['vertical'] += (destination['aim'] * increment)
        elif (direction == 'up'):
            destination['aim'] -= increment
        elif (direction == 'down'):
            destination['aim'] += increment

    print(destination)
    print(destination['horizontal'] * destination['vertical'])


if __name__ == "__main__":
    main()
