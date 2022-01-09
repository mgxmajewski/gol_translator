import pytest
from assertpy import assert_that
from .utils.rle_translator import expand_row


# Create your tests here.
class TestUtil:

    def test_expand_row_simple_chars(self):
        row = ['oo']
        result = expand_row(row)

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
    def prepare_expand_row(self):
        self.expand_row = expand_row

        # case 1
        row_1 = ['2bo2b2o']
        expected_1 = ['2b', 'o', '2b', '2o']
        case_row_1 = row_1, expected_1

        # case 2
        row_2 = ['112bo2b2o']
        expected_2 = ['112b', 'o', '2b', '2o']
        case_row_2 = row_2, expected_2

    @pytest.mark.parametrize("row_provided, expected", [case_row_1, case_row_2])
    def test_expand_row_int_char_notation(self, row_provided, expected):
        result = expand_row(row_provided)

        assert_that(result).is_equal_to(expected)
