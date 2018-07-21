from unittest import TestCase
from ..build import q03_twitter_plt1
from inspect import getfullargspec




class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q03_twitter_plt1).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

