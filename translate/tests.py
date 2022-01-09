import pytest
from assertpy import assert_that
from .utils.rle_translator import parse_row, row_expand


# Create your tests here.
class TestUtilParser:

    def test_parse_row_simple_chars(self):
        row = ['oo']
        result = parse_row(row)

        expected = ['o', 'o']
        assert_that(result).is_equal_to(expected)

    # case 1
    row_1 = ['2bo2b2o']
    expected = ['2b', 'o', '2b', '2o']
    case_row_1 = row_1, expected

    # case 2
    row_2 = ['112bo2b2o']
    expected_2 = ['112b', 'o', '2b', '2o']
    case_row_2 = row_2, expected_2

    @pytest.fixture(autouse=True)
    def prepare_parse_row(self):
        self.parse_row = parse_row

    @pytest.mark.parametrize("row_provided, expected", [case_row_1, case_row_2])
    def test_parse_row_int_char_notation(self, row_provided, expected):
        result = parse_row(row_provided)

        assert_that(result).is_equal_to(expected)
