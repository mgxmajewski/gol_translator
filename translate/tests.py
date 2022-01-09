import pytest
from assertpy import assert_that
from .utils.rle_translator import extract_rows, row_parse, row_expand


class TestUtil:

    def test_parse_row_simple_chars(self):
        row = ['oo']
        result = row_parse(row)
        expected = ['o', 'o']
        assert_that(result).is_equal_to(expected)

    # case 1
    row_1 = ['2bo2b2o']
    expected_1 = ['2b', 'o', '2b', '2o']
    case_row_1 = row_1, expected_1

    # case 2
    row_2 = ['112bo2b2o']
    expected_2 = ['112b', 'o', '2b', '2o']
    case_row_2 = row_2, expected_2

    @pytest.fixture(autouse=True)
    def prepare_parse_row(self):
        self.parse_row = row_parse

    @pytest.mark.parametrize("row_provided, expected", [case_row_1, case_row_2])
    def test_parse_row_int_char_notation(self, row_provided, expected):
        result = row_parse(row_provided)
        assert_that(result).is_equal_to(expected)

    # case 1
    row_1 = ['2b', 'o', '2b', '2o']
    expected_1 = ['b', 'b', 'o', 'b', 'b', 'o', 'o']
    case_row_1 = row_1, expected_1

    # case 2
    row_2 = ['12b', 'o', '2b', '2o']
    expected_2 = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'o', 'b', 'b', 'o', 'o']
    case_row_2 = row_2, expected_2

    @pytest.fixture(autouse=True)
    def prepare_expand_row(self):
        self.expand_row = row_expand

    @pytest.mark.parametrize("row_provided, expected", [case_row_1, case_row_2])
    def test_expand_row(self, row_provided, expected):
        result = row_expand(row_provided)
        assert_that(result).is_equal_to(expected)
