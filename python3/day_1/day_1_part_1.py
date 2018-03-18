def get_num_pairs(circular_list):
    """
    Generate a list of pairs:
    [(n, n+1), (n+1, n+2), ..., (n-1, n)]
    """
    list_offset = circular_list[1:] + circular_list[0:1]
    for number_pair in zip(circular_list, list_offset):
        yield tuple(map(int, number_pair))


def sum_diget_matches(circular_list):
    total_sum = 0
    for num1, num2 in get_num_pairs(circular_list):
        if num1 == num2:
            total_sum += num1
    return total_sum


if __name__ == '__main__':
    with open('input.txt') as input_file:
        input_text = input_file.readlines()[0].strip()
    print(sum_diget_matches(input_text))
