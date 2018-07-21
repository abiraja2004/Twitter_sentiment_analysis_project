from unittest import TestCase
from ..build import q04_twitter_plt2
from inspect import getfullargspec




class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q04_twitter_plt2).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

