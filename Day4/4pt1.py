import copy
import sys


def fetch_input(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()

    return \
        [int(number.strip()) for number in numbers[0].split(',')], \
        [row.split() for row in list(filter(lambda x: x != '\n', numbers[1:]))]


def main():
    to_draw_numbers, boards_rows_list = fetch_input('input_files/4_test.txt')
    print(to_draw_numbers)

    # Convert individual cells to dicts with True/False as value to depict whether they've been drawn or not
    new_board = []
    for row in boards_rows_list:
        new_row = []
        for val in row:
            new_row.append({int(val): False})

        new_board.append(new_row)

    count = 0
    boards = []
    while count < len(new_board):
        # board = [[{22: False}, {13: False}, {17: False}, {11: False}, {0: False}], [{8: False}, {2: False}, ...]
        board = new_board[count:count + 5]
        boards.append(board)
        count += 5

    for number in to_draw_numbers:
        boards = update_boards(boards, number)  # switch False to True when a good number was drawn
        winning_board = find_winning_board(boards)

        if len(winning_board) > 0:
            print(f"Winning board! --> {winning_board}")
            final_score = calculate_final_score(winning_board, number)
            print(final_score)
            boards.remove(winning_board)
            break


def is_all_true(row: list) -> bool:
    for cell in row:
        for _, v in cell.items():
            if v == False:
                return False

    return True


def find_winning_board(boards: list) -> list:
    for board in boards:
        # Any full rows?
        for i in range(0, 5):
            if is_all_true(board[i]):
                return board

        # Any full columns?
        for i in range(0, 5):
            column = []
            for j in range(0, 5):
                column.append(board[j][i])

            if is_all_true(column):
                return board

    return []


def calculate_final_score(board: list, last_number: int) -> int:
    score = 0
    for row in board:
        for cell in row:
            for k, v in cell.items():
                # Final score is the sum of all not drawn numbers on the board...
                if v == False:
                    score += int(k)
    # ... times the last_number drawn
    return score * last_number


def update_boards(boards: list, number: int) -> list:
    # Flips a found number on a board to True...
    # damn inefficient searching :)
    for board in boards:
        for row in board:
            for val in row:
                for k, v in val.items():
                    if k == number:
                        val.update({k: True})

    return boards


if __name__ == "__main__":
    main()
