import pytest
from assertpy import assert_that
from .utils.rle_translator import extract_rows, extract_expressions, row_expand, clean_rle, rle_to_2d_array


class TestUtil:

    # case 1
    rle_1 = 'bob$2bo$3o'
    expected_1 = [['bob'], ['2bo'], ['3o']]
    case_1 = rle_1, expected_1

    @pytest.fixture(autouse=True)
    def prepare_extract_rows(self):
        self.extract_rows = extract_rows

    @pytest.mark.parametrize("rle_provided, expected", [case_1])
    def test_extract_rows(self, rle_provided, expected):
        result = extract_rows(rle_provided)
        assert_that(result).is_equal_to(expected)

    def test_extract_expressions_simple_chars(self):
        row = ['oo']
        result = extract_expressions(row)
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
    def prepare_extract_expressions(self):
        self.extract_expressions = extract_expressions

    @pytest.mark.parametrize("row_provided, expected", [case_row_1, case_row_2])
    def test_extract_expressions_int_char_notation(self, row_provided, expected):
        result = extract_expressions(row_provided)
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

    def test_clean_rle(self):
        rle = '2bo2b2o!'
        result = clean_rle(rle)
        expected = '2bo2b2o'
        assert_that(result).is_equal_to(expected)

    def test_rle_to_2d_array(self):
        rle = 'bob$2bo$3o!'
        result = rle_to_2d_array(rle)
        expected = [['b', 'o', 'b'], ['b', 'b', 'o'], ['o', 'o', 'o']]
        assert_that(result).is_equal_to(expected)
