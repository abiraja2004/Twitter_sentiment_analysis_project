import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q03_tweet_info
from inspect import getfullargspec
import pandas

info1, info2, info3 = q03_tweet_info()


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getfullargspec(q03_tweet_info).args
        self.assertEqual(len(arg), 0, "Expected argument(s) %d, Given %d" % (0, len(arg)))

    def test_instance(self):
        self.assertIsInstance(info1, pandas.core.series.Series,
                              "The Expected return type does not match with the given return type")

    def test_instance_1(self):
        self.assertIsInstance(info2, pandas.core.series.Series,
                              "The Expected return type does not match with the given return type")

    def test_instance_2(self):
        self.assertIsInstance(info3, pandas.core.series.Series,
                              "The Expected return type does not match with the given return type")
