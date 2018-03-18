from typing import List


def checksum_line(numbers_list: iter) -> int:
    """
    Given a list of numbers, return the value of the maximum - minimum values
    """
    min_number = max_number = numbers_list[0]
    for number in numbers_list[1:]:
        min_number = min(min_number, number)
        max_number = max(max_number, number)
    return max_number - min_number


def get_number_list_from_line(number_list_string: str) -> List[int]:
    return list(map(int, number_list_string.split()))


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