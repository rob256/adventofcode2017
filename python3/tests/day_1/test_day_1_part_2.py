import pytest

from day_1 import day_1_part_2


@pytest.mark.parametrize(('number_list', 'expected'), [
    ('1212', [(1, 1), (2, 2), (1, 1), (2, 2)]),
])
def test_get_number_pairs(number_list, expected):
    output = list(day_1_part_2.get_number_pairs(number_list))
    assert output == expected


@pytest.mark.parametrize(('number_list', 'expected'), [
    ('1212', 6),
    ('1122', 0),
    ('123425', 4),
    ('123123', 12),
    ('12131415', 4),
])
def test_sum_digit_matches(number_list, expected):
    output = day_1_part_2.sum_digit_matches(number_list)
    assert output == expected