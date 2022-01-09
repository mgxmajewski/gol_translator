from django.test import TestCase
from .utils.rle_translator import expand_row


# Create your tests here.
class UtilTest(TestCase):

    def test_expand_row_simple_chars(self):
        row = ['oo']
        result = expand_row(row)

        self.assertEqual(result, ['o', 'o'])

    def test_expand_row_int_char_notation(self):
        row = ['2bo2b2o']
        result = expand_row(row)

        self.assertEqual(result, ['2b', 'o', '2b', '2o'])
