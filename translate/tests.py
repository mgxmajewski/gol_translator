import pytest
from django.test import TestCase
from .utils.rle_translator import expand_row


# Create your tests here.
class UtilTest(TestCase):

    def test_expand_row_simple_chars(self):
        row = ['oo']
        result = expand_row(row)

        self.assertEqual(result, ['o', 'o'])

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

    def test_expand_row_int_char_notation_1(self):
        row = ['2bo2b2o']
        expected = ['2b', 'o', '2b', '2o']
        result = expand_row(row)

        self.assertEqual(result, expected)
