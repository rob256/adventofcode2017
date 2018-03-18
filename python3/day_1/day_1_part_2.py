from typing import List, Tuple


def get_number_pairs(number_list: str) -> List[Tuple[int, int]]:
    mid = len(number_list) // 2
    repeat_list = number_list[mid:] + number_list[:mid]
    for number_pair in zip(number_list, repeat_list):
        yield tuple(map(int, number_pair))


def sum_digit_matches(circular_list: iter) -> int:
    total_sum = 0
    for num1, num2 in get_number_pairs(circular_list):
        if num1 == num2:
            total_sum += num1
    return total_sum


def main():
    with open('input.txt') as input_file:
        input_text = input_file.readlines()[0].strip()
    print(sum_digit_matches(input_text))


if __name__ == '__main__':
    main()
