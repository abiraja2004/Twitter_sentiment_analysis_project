import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_twitter_plt2
from inspect import getfullargspec


q05_twitter_plt2()


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q05_twitter_plt2).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

