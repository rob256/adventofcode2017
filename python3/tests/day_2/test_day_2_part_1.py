import pytest

from day_2 import day_2_part_1


@pytest.mark.parametrize(('numbers_list', 'expected'), [
    ([1, 2, 3, 4], 3),
    ([4, 3, 2, 1], 3),
    ([4, 3, 2, 1], 3),
    ([5, 5], 0),
    ([1, 5], 4),
])
def test_checksum_line(numbers_list, expected):
    output = day_2_part_1.checksum_line(numbers_list)
    assert output == expected


NUMBERS_INPUT = """1 2 3
5 5 4
1 9 1
9 1 9"""


def test_checksum_spreadsheet():
    assert day_2_part_1.checksum_spreadsheet(NUMBERS_INPUT) == 19


@pytest.mark.parametrize(('number_list_string', 'expected'), [
    ('1 2 3', [1, 2, 3]),
    (' 4  5  6  ', [4, 5, 6]),
])
def test_get_number_list_from_line(number_list_string, expected):
    output = day_2_part_1.get_number_list_from_line(number_list_string)
    assert output == expected
