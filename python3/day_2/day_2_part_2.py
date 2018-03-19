from typing import List

from day_2.day_2_part_1 import get_number_list_from_line


def checksum_line(numbers_list: iter) -> int:
    """
    Given a list of numbers, find 2 numbers which divide evenly.

    We can double loop, but this will be O(n^2) complexity, I'm
    going to lower this slightly by sorting the list first.
    """
    sorted_number_list = sorted(numbers_list)
    left_index = 0
    right_index = len(sorted_number_list) - 1

    # Given a list, sort it and then only check the numbers which have a
    # chance of being a factor
    while left_index < right_index:
        left_num = sorted_number_list[left_index]
        right_num = sorted_number_list[right_index]
        if left_num > right_num / 2:
            right_index -= 1
            left_index = 0
            continue
        if right_num % left_num == 0:
            return right_num // left_num
        else:
            left_index += 1

    raise ValueError('No factors found.')


def checksum_spreadsheet(spreadsheet_string: str) -> int:
    total_checksum = 0
    for number_list_string in spreadsheet_string.split('\n'):
        number_list = get_number_list_from_line(number_list_string)
        total_checksum += checksum_line(number_list)
    return total_checksum


def main():
    with open('input.txt') as input_file:
        input_text = input_file.read().rstrip()
    print(checksum_spreadsheet(input_text))


if __name__ == '__main__':
    main()
