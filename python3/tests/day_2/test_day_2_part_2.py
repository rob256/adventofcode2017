import pytest

from day_2 import day_2_part_2


@pytest.mark.parametrize(('number_list', 'expected'), [
    ([2, 3, 4, 5], 2),
    ([3, 2, 5, 4], 2),
    ([10, 5, 12, 19], 2),
    ([39, 5, 12, 25], 5),
])
def test_checksum_line(number_list, expected):
    output = day_2_part_2.checksum_line(number_list)
    assert output == expected


def test_checksum_failure():
    number_list = [3, 4, 5]
    with pytest.raises(ValueError) as e:
        day_2_part_2.checksum_line(number_list)