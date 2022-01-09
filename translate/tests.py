from django.test import TestCase
from .utils.rle_translator import expand_row


# Create your tests here.
class UtilTest(TestCase):

    def test_expand_row_simple_chars(self):
        row = ['oo']
        result = expand_row(row)

        self.assertEqual(result, ['o', 'o'])
