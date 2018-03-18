import pytest

from day_1 import day_1_part_1


def test_get_number_pairs():
    assert list(day_1_part_1.get_num_pairs([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4), (4, 1)]


@pytest.mark.parametrize(('circular_list', 'expected'), [
    ('1122', 3),
    ('1234', 0),
    ('1111', 4),
])
def test_sum_digit_matches(circular_list, expected):
    output = day_1_part_1.sum_diget_matches(circular_list)
    assert output == expected